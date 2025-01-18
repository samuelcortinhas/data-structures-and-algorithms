from typing import List


# Definition for a pair.
class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value


class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        if len(pairs) <= 1:
            return pairs

        mid = len(pairs) // 2
        left = pairs[mid:]
        right = pairs[:mid]

        left_sorted = self.mergeSort(left)
        right_sorted = self.mergeSort(right)

        i, j = 0, 0
        res = []
        while i < len(left_sorted) and j < len(right_sorted):
            if left_sorted[i].key <= right_sorted[j].key:
                res.append(left_sorted[i])
                i += 1
            else:
                res.append(right_sorted[j])
                j += 1

        res += left_sorted[i:] + right_sorted[j:]
        return res
