from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # Time O(n^2), Memory O(1)
        n = len(gas)
        for i in range(n):
            tank = gas[i]
            if not tank:
                continue
            stop = False
            for j in range(n):
                tank -= cost[(i + j) % n]
                if tank < 0:
                    stop = True
                    break
                tank += gas[(i + j + 1) % n]
            if not stop:
                return i
        return -1
