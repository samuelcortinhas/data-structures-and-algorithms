from typing import List


class Solution:
    # Time O(n log n), Memory O(n)
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # time = (target - position) / speed
        stack = [-1]
        for p, s in sorted(zip(position, speed))[::-1]:
            t = (target - p) / s
            if t > stack[-1]:
                stack.append(t)
        return len(stack) - 1

    # def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
    #     # no stack, just use counter
    #     max_t = 0
    #     fleets = 0
    #     for p, s in sorted(zip(position, speed))[::-1]:
    #         t = (target - p) / s
    #         if t > max_t:
    #             fleets += 1
    #             max_t = t
    #     return fleets
