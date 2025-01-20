from typing import List


class Solution:
    # Bad question

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Time O(n), Memory O(1) (excluding answer)
        answer = [1] * len(nums)

        left = 1
        for i in range(len(nums)):
            answer[i] = left
            left *= nums[i]

        right = 1
        for i in range(len(nums) - 1, -1, -1):
            answer[i] *= right
            right *= nums[i]

        return answer

    # def productExceptSelfV1(self, nums: List[int]) -> List[int]:
    #     # Time O(n), Memory O(n)
    #     prefix = [1 for _ in range(len(nums))]
    #     left = 1
    #     for i, n in enumerate(nums):
    #         prefix[i] = left
    #         left *= n

    #     postfix = [1 for _ in range(len(nums))]
    #     right = 1
    #     for i, n in enumerate(nums[::-1]):
    #         postfix[i] = right
    #         right *= n

    #     return [i * j for i, j in zip(prefix, postfix[::-1])]
