# from collections import Counter
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Boyer–Moore majority vote algorithm
        # Time O(n), Memory O(1)
        maj_num, count = 0, 0
        for n in nums:
            if count == 0:
                maj_num = n
            count += 1 if n == maj_num else -1
        return maj_num

    # def majorityElementSort(self, nums: List[int]) -> int:
    #     # Time O(n log n), Memory O(n)
    #     counter = Counter(nums)
    #     s = sorted(counter.items(), key=lambda x: x[1], reverse=True)
    #     return s[0][0]
