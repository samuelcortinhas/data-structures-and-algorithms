from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Time O(4^n), Memory O(4^n)
        phone_map = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        nums = list(digits)
        res = []
        stack = []

        def dfs(i):
            if i >= len(digits):
                res.append(list(stack))
                return
            for char in phone_map[nums[i]]:
                stack.append(char)
                dfs(i + 1)
                stack.pop()

        dfs(0)
        return ["".join(r) for r in res if r]
