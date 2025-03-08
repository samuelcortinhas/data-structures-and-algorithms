class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # Time O(n), Memory O(1)
        curr = sum([1 for b in blocks[:k] if b == "B"])
        max_num = curr
        for i in range(k, len(blocks)):
            curr += blocks[i] == "B"
            curr -= blocks[i - k] == "B"
            max_num = max(max_num, curr)
        return max(k - max_num, 0)
