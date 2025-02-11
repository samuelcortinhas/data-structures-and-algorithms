from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Time O(n), O(1)
        i = len(digits) - 1
        while i >= 0:
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
            i -= 1
        return [1] + digits

    # def plusOne(self, digits: List[int]) -> List[int]:
    #     # Time O(n), O(1)
    #     if digits[-1] < 9:
    #         digits[-1] += 1
    #         return digits

    #     digits = digits[::-1]
    #     rem = 1
    #     for i in range(len(digits)):
    #         d = digits[i]
    #         if d == 9:
    #             digits[i] = 0
    #         else:
    #             digits[i] += 1
    #             rem = 0
    #             break
    #     if rem:
    #         digits.append(1)
    #     return digits[::-1]

    # def plusOne(self, digits: List[int]) -> List[int]:
    #     # Time O(n), O(n)
    #     if digits[-1] < 9:
    #         digits[-1] += 1
    #         return digits
    #     else:
    #         rem = 1
    #         res = [0]
    #         for d in digits[-2::-1]:
    #             res.append((d + rem) % 10)
    #             rem = (d + rem) // 10
    #         if rem:
    #             res.append(1)
    #         return res[::-1]
