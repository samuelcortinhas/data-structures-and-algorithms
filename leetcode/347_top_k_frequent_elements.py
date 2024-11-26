from collections import Counter
from itertools import chain, islice


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # "Bucket sort"
        # Time O(n), Memory O(n)
        counts = Counter(nums)

        freqs = [[] for _ in range(len(nums) + 1)]
        for n, v in counts.items():
            freqs[v].append(n)

        top = chain(*freqs[::-1])
        topk = islice(top, k)
        return list(topk)

    # def topKFrequentDirect(self, nums, k):
    #     # Time O(n log n), Memory O(n)
    #     counts = Counter(nums)
    #     l = list(counts.items())
    #     l.sort(key=lambda x: x[1], reverse=True)
    #     return [u[0] for u in l[:k]]


if __name__ == "__main__":
    x = [4, 1, -1, 2, -1, 2, 3]
    print(Solution().topKFrequent(x, 2))
