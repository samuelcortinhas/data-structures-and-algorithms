from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Time O(n), Memory O(1)
        i = 0
        j = len(numbers) - 1
        while True:
            s = numbers[i] + numbers[j]
            if s < target:
                i += 1
            elif s > target:
                j -= 1
            else:
                return [i + 1, j + 1]
