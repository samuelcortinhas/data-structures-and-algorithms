from typing import List


class Solution:
    # top down dp
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # Time O(365*n), Memory O(365*n), where n=len(days)
        tickets = {0: 1, 1: 7, 2: 30}  # index: pass length
        dp = {}

        def dfs(i, covered_until):
            if i == len(days):
                return 0
            if (i, covered_until) in dp:
                return dp[(i, covered_until)]
            if covered_until >= days[i]:
                dp[(i, covered_until)] = dfs(i + 1, covered_until)
                return dp[(i, covered_until)]

            best = float("inf")
            for j, c in enumerate(costs):
                if (new := c + dfs(i + 1, days[i] + tickets[j] - 1)) < best:
                    best = new

            dp[(i, covered_until)] = best
            return dp[(i, covered_until)]

        return dfs(0, 0)

    # # brute force on ternary decision tree
    # def mincostTickets(self, days: List[int], costs: List[int]) -> int:
    #     # Time O(3^n), Memory O(3^n), where n=len(days)
    #     tickets = {0: 1, 1: 7, 2: 30}  # index: pass length

    #     def dfs(i, covered_until, curr_cost):
    #         if i == len(days):
    #             return curr_cost
    #         if covered_until >= days[i]:
    #             return dfs(i + 1, covered_until, curr_cost)

    #         return min(
    #             [
    #                 dfs(i + 1, days[i] + tickets[j] - 1, curr_cost + c)
    #                 for j, c in enumerate(costs)
    #             ]
    #         )

    #     return dfs(0, 0, 0)
