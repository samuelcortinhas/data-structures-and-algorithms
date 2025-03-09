from collections import defaultdict
from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # Time O(V+E), Memory O(V)
        in_degree = [0] * n
        out_degree = [0] * n
        for a, b in trust:
            out_degree[a - 1] += 1
            in_degree[b - 1] += 1

        for i in range(n):
            if in_degree[i] == n - 1 and out_degree[i] == 0:
                return i + 1
        return -1

    # def findJudge(self, n: int, trust: List[List[int]]) -> int:
    #     # Time O(V+E), Memory O(V+E)
    #     if n == 1:
    #         return 1
    #     if not trust:
    #         return -1

    #     adj_list = defaultdict(list)
    #     for a, b in trust:
    #         adj_list[b].append(a)

    #     for k, v in adj_list.items():
    #         if len(v) == n - 1:
    #             valid = True
    #             for x in v:
    #                 if k in adj_list[x]:
    #                     valid = False
    #                     break
    #             if valid:
    #                 return k
    #     return -1
