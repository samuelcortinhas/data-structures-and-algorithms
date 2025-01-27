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
