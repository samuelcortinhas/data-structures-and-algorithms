class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # Time O(n), Memory O(1)
        curr = blocks[:k].count("B")
        max_num = curr
        for i in range(k, len(blocks)):
            curr += (blocks[i] == "B") - (blocks[i - k] == "B")
            max_num = max(max_num, curr)
        return max(k - max_num, 0)
