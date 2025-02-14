import heapq
from collections import Counter
from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # Time O(n log n), Memory O(n) where n=len(hand), k = groupSize
        if (len(hand) % groupSize) != 0:
            return False

        counts = Counter(hand)
        heap = list(hand)
        heapq.heapify(heap)
        while heap:
            start = heapq.heappop(heap)
            if not counts[start]:
                continue

            for i in range(groupSize):
                if counts[start + i]:
                    counts[start + i] -= 1
                else:
                    return False
        return True
