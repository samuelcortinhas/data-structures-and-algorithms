class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Time O(n), Memory O(n)
        d = set()
        for x in nums:
            if x in d:
                return True
            d.add(x)
        return False
