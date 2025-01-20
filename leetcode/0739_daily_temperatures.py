from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Time O(n), Memory O(n)
        answer = [0] * len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            while stack and (t > stack[-1][0]):
                answer[stack[-1][1]] = i - stack[-1][1]
                stack.pop()
            stack.append((t, i))
        return answer

    # def dailyTemperaturesV1(self, temperatures: List[int]) -> List[int]:
    #     # Time O(n), Memory O(n)
    #     answer = [0] * len(temperatures)
    #     stack = [(temperatures[0], 0)]

    #     i = 1
    #     while i < len(temperatures):
    #         while stack and (temperatures[i] > stack[-1][0]):
    #             answer[stack[-1][1]] = i - stack[-1][1]
    #             stack.pop()

    #         stack.append((temperatures[i], i))
    #         i += 1

    #     return answer
