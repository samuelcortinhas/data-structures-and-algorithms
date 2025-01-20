from collections import Counter, defaultdict


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Time O(n), Memory O(1)
        return Counter(s) == Counter(t)

    def isAnagramAlt(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Time O(n), Memory O(1)
        ds = defaultdict(int)
        dt = defaultdict(int)
        for x in s:
            ds[x] += 1
        for y in t:
            dt[y] += 1

        return ds == dt
