from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # Time O(n), Memory O(n), where n = len(operations)
        stack = []
        for op in operations:
            if op == "C":
                stack.pop()
            elif op == "D":
                stack.append(stack[-1] * 2)
            elif op == "+":
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(op))
        return sum(stack)
