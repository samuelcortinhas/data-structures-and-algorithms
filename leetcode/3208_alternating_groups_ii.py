from typing import List


class Solution:
    # brute force
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        # Time O(n*k) , Memory O(1)
        n = len(colors)
        res = 0
        for i in range(len(colors)):
            for j in range(k - 1):
                if colors[(i + j + 1) % n] == colors[(i + j) % n]:
                    res -= 1
                    break
            res += 1
        return res
