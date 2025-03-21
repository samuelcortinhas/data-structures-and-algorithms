from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Time O(4^n), Memory O(4^n)
        phone_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        res = []

        def backtrack(i, stack):
            if len(stack) == len(digits):
                res.append("".join(stack))
                return

            for c in phone_map[digits[i]]:
                stack.append(c)
                backtrack(i + 1, stack)
                stack.pop()

        backtrack(0, [])
        return res if digits else []


# class Solution:
#     def letterCombinations(self, digits: str) -> List[str]:
#         # Time O(4^n), Memory O(4^n)
#         phone_map = {
#             "2": "abc",
#             "3": "def",
#             "4": "ghi",
#             "5": "jkl",
#             "6": "mno",
#             "7": "pqrs",
#             "8": "tuv",
#             "9": "wxyz",
#         }
#         nums = list(digits)
#         res = []
#         stack = []

#         def dfs(i):
#             if i >= len(digits):
#                 res.append(list(stack))
#                 return
#             for char in phone_map[nums[i]]:
#                 stack.append(char)
#                 dfs(i + 1)
#                 stack.pop()

#         dfs(0)
#         return ["".join(r) for r in res if r]
