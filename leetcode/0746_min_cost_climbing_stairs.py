from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Time O(n), Memory O(1)
        prev, curr = cost[0], cost[1]
        for i in range(2, len(cost)):
            tmp = curr
            curr = min(prev, curr) + cost[i]
            prev = tmp
        return min(prev, curr)
