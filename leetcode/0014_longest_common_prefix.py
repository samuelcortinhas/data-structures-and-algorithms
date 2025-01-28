from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Time O(n*m), Memory O(n) where n = len(strs), m = max string length
        common = strs[0]
        for s in strs:
            for i, c in enumerate(common):
                try:
                    if s[i] != c:
                        common = common[:i]
                        break
                except:
                    common = common[:i]
                    continue
        return common
