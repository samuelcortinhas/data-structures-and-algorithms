from collections import defaultdict
from typing import List


class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.height = [0] * n

    def find(self, node):
        p = self.par[node]
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p

    def union(self, node1, node2):
        p1, p2 = self.find(node1), self.find(node2)
        if p1 == p2:
            return False
        if self.height[p1] > self.height[p2]:
            self.par[p2] = p1
        elif self.height[p1] < self.height[p2]:
            self.par[p1] = p2
        else:
            self.par[p2] = p1
            self.height[p1] += 1
        return True


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # Time O(n), Memory O(n) where n = num emails total
        uf = UnionFind(len(accounts))
        email_to_account = {}  # email to account index
        for i, a in enumerate(accounts):
            for e in a[1:]:
                if e in email_to_account:
                    uf.union(i, email_to_account[e])
                else:
                    email_to_account[e] = i

        account_to_emails = defaultdict(list)  # account index to emails
        for e, i in email_to_account.items():
            rep = uf.find(i)  # find representative
            account_to_emails[rep].append(e)

        res = []
        for i, e in account_to_emails.items():
            name = accounts[i][0]
            res.append([name] + sorted(e))  # format output
        return res
