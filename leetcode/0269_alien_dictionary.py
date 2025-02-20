from collections import defaultdict
from typing import List


class Solution:
    # Time O(n), Memory O(n) where n=len(words)
    def alienOrder(self, words: List[str]) -> str:
        # idea: compare adjacent words for first position where characters differ
        # construct graph of pre-reqs and do topological sort with cycle detection
        adj_list = defaultdict(set)
        alphabet = set([c for word in words for c in word])
        for i in range(1, len(words)):
            word1 = words[i - 1]
            word2 = words[i]
            skip = False
            for c1, c2 in zip(word1, word2):
                if c1 != c2:
                    adj_list[c1].add(c2)
                    skip = True
                    break
            if not skip and len(word1) > len(word2):
                return ""

        # topological sort
        res = []
        visit = set()
        cycle = False

        def dfs(node):
            nonlocal cycle
            if node in path:
                cycle = True
                return
            if node in visit:
                return
            path.add(node)
            visit.add(node)
            for neigh in adj_list[node]:
                dfs(neigh)
            res.append(node)
            path.remove(node)

        for c in alphabet:
            path = set()
            dfs(c)

            if cycle:
                return ""

            if len(res) == len(alphabet):
                return "".join(res[::-1])

        if len(res) != len(alphabet):
            res.extend(list(alphabet.difference(set(res))))
            return "".join(res[::-1])
