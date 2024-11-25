from collections import Counter, defaultdict


class Solution(object):
    def getAnagramSignature(self, chars):
        """
        Compute an anagram invariant signature on string of characters
        """
        # Time O(m), Memory O(1)
        counts = [0] * 26
        for x in chars:
            counts[ord(x) - ord("a")] += 1
        return tuple(counts)  # tuple is hashable and valid as dict key

    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # Time O(nm), Memory O(nm)
        seen = defaultdict(list)
        for x in strs:
            sig = self.getAnagramSignature(x)
            seen[sig].append(x)
        return list(seen.values())

    # def getAnagramSignatureShorter(self, chars):
    #     """
    #     Computes an anagram invariant signature on a string of characters
    #     """
    #     # Time O(m), Memory O(log(m))
    #     c = Counter(chars)
    #     sig = ""
    #     for i in range(26):
    #         k = chr(ord("a") + i)
    #         v = c.get(k, 0)
    #         if v > 0:
    #             sig = sig + "{}{}".format(k, str(v))
    #     return sig

    # def groupAnagrams(self, strs):
    #     """
    #     :type strs: List[str]
    #     :rtype: List[List[str]]
    #     """
    #     # Time O(nm log(m)), Memory O(nm)
    #     seen = defaultdict(list)
    #     for x in strs:
    #         s = "".join(sorted(x))  # use sorted characters as signature
    #         seen[s].append(x)
    #     return list(seen.values())
