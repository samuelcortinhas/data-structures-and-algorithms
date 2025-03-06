from typing import List


class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        # Time O(n^2), Memory O(n^2)
        n = len(grid)
        seen = set()
        a, b = None, None
        for row in grid:
            for v in row:
                if v in seen:
                    a = v
                seen.add(v)

        (b,) = set(range(1, 1 + n * n)).difference(seen)
        return [a, b]
