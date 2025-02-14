from typing import List


class Solution:
    def canCompleteCircuitV3(self, gas: List[int], cost: List[int]) -> int:
        # Time O(n), Memory O(n)
        n = len(gas)
        dp = [g - c for g, c in zip(gas, cost)]
        tank = 0
        window_length = 0
        for i in range(2 * n):
            tank += dp[i % n]
            window_length += 1
            if tank >= 0 and window_length == n:
                return (i + 1) % n
            if tank < 0:
                tank = 0
                window_length = 0
                continue
        return -1

    # def canCompleteCircuitV2(self, gas: List[int], cost: List[int]) -> int:
    #     # Time O(n^2), Memory O(n)
    #     n = len(gas)
    #     diff = [g - c for g, c in zip(gas, cost)]
    #     print(diff)
    #     for i in range(n):
    #         tank = 0
    #         for j in range(n):
    #             tank += diff[(i + j) % n]
    #             if tank < 0:
    #                 break
    #         if tank >= 0:
    #             return i
    #     return -1

    # def canCompleteCircuitV1(self, gas: List[int], cost: List[int]) -> int:
    #     # Time O(n^2), Memory O(1)
    #     n = len(gas)
    #     for i in range(n):
    #         tank = gas[i]
    #         if not tank:
    #             continue
    #         stop = False
    #         for j in range(n):
    #             tank -= cost[(i + j) % n]
    #             if tank < 0:
    #                 stop = True
    #                 break
    #             tank += gas[(i + j + 1) % n]
    #         if not stop:
    #             return i
    #     return -1
