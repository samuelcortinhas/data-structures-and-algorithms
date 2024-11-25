from collections import Counter


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # Time O(n log n), Memory O(n)
        counts = Counter(nums)
        l = list(counts.items())
        l.sort(key=lambda x: x[1], reverse=True)
        return [u[0] for u in l[:k]]


if __name__ == "__main__":
    x = [4, 1, -1, 2, -1, 2, 3]
    print(Solution().topKFrequent(x, 2))
