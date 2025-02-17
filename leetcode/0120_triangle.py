from typing import List


class Solution:
    # Too slow
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # Time O(2^n), Memory O(n) where n = #rows
        def dfs(row_index, level):  # post order traversal but repeated work
            if level == (len(triangle) - 1):
                return triangle[level][row_index]
            l = dfs(row_index, level + 1)
            r = dfs(row_index + 1, level + 1)
            return triangle[level][row_index] + min(l, r)

        return dfs(0, 0)


# class Solution:
#     # Too slow
#     def minimumTotal(self, triangle: List[List[int]]) -> int:
#         res = float("inf")

#         def dfs(row_index, level, path_sum):
#             # Time O(2^n), Memory O(n) where n = #rows
#             nonlocal res
#             path_sum += triangle[level][row_index]
#             if level == (len(triangle) - 1):
#                 res = min(res, path_sum)
#                 return
#             dfs(row_index, level + 1, path_sum)
#             dfs(row_index + 1, level + 1, path_sum)

#         dfs(0, 0, 0)
#         return res
