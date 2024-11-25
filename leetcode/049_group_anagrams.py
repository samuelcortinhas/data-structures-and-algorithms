from collections import defaultdict


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # Time O(nm log(m)), Memory O(nm)
        seen = defaultdict(list)
        for x in strs:
            s = "".join(sorted(x))
            seen[s].append(x)
        return list(seen.values())
