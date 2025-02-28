class Solution:
    # top down dp with memoisation
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # Time O(n*m), Memory O(n*m) where n=len(s1), m=len(s2)
        if len(s1) + len(s2) != len(s3):
            return False

        dp = {}

        def backtrack(i, j):
            if (i, j) in dp:
                return dp[(i, j)]
            if i == len(s1) and j == len(s2):
                return True
            elif i == len(s1):
                if s2[j] == s3[i + j]:
                    return backtrack(i, j + 1)
                else:
                    return False
            elif j == len(s2):
                if s1[i] == s3[i + j]:
                    return backtrack(i + 1, j)
                else:
                    return False

            if s1[i] == s3[i + j] and s2[j] != s3[i + j]:
                dp[(i, j)] = backtrack(i + 1, j)
            elif s1[i] != s3[i + j] and s2[j] == s3[i + j]:
                dp[(i, j)] = backtrack(i, j + 1)
            elif s1[i] == s3[i + j] and s2[j] == s3[i + j]:
                dp[(i, j)] = backtrack(i + 1, j) or backtrack(i, j + 1)
            else:
                dp[(i, j)] = False
            return dp[(i, j)]

        return backtrack(0, 0)

    # # brute force
    # def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
    #     # Time O(2^n), Memory O(2^n) where n=len(s3)
    #     if len(s1) + len(s2) != len(s3):
    #         return False

    #     def backtrack(i, j):
    #         if i == len(s1) and j == len(s2):
    #             return True
    #         elif i == len(s1):
    #             if s2[j] == s3[i + j]:
    #                 return backtrack(i, j + 1)
    #             else:
    #                 return False
    #         elif j == len(s2):
    #             if s1[i] == s3[i + j]:
    #                 return backtrack(i + 1, j)
    #             else:
    #                 return False

    #         if s1[i] == s3[i + j] and s2[j] != s3[i + j]:
    #             return backtrack(i + 1, j)
    #         elif s1[i] != s3[i + j] and s2[j] == s3[i + j]:
    #             return backtrack(i, j + 1)
    #         elif s1[i] == s3[i + j] and s2[j] == s3[i + j]:
    #             return backtrack(i + 1, j) or backtrack(i, j + 1)
    #         else:
    #             return False

    #     return backtrack(0, 0)
