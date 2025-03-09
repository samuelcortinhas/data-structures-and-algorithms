from collections import defaultdict
from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # Time O(V+E), Memory O(V+E)
        if n == 1:
            return 1
        if not trust:
            return -1

        adj_list = defaultdict(list)
        for a, b in trust:
            adj_list[b].append(a)

        for k, v in adj_list.items():
            if len(v) == n - 1:
                valid = True
                for x in v:
                    if k in adj_list[x]:
                        valid = False
                        break
                if valid:
                    return k
        return -1
