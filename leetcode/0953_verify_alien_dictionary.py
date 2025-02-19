from typing import List


class Solution:
    # Time O(m*n), Memory O(26), where n=len(words), m=max(len(word))
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # compare consecutive words
        char_index = {c: i for i, c in enumerate(order)}
        for j in range(1, len(words)):
            skip = False
            for a, b in zip(words[j - 1], words[j]):
                if char_index[a] < char_index[b]:
                    skip = True
                    break
                elif char_index[a] > char_index[b]:
                    return False
            if not skip and len(words[j - 1]) > len(words[j]):
                return False
        return True
