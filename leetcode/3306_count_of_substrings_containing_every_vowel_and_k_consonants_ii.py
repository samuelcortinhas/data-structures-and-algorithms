class Solution:
    # first attempt - doesn't pass all tests
    def countOfSubstrings(self, word: str, k: int) -> int:
        # Time O(n), Memory O(1)
        counts = [0] * 6  # (a,e,i,o,u,consonants)
        char_map = {"a": 0, "e": 1, "i": 2, "o": 3, "u": 4}
        left = 0
        res = 0
        for right in range(len(word)):
            counts[char_map.get(word[right], 5)] += 1
            while counts[-1] > k:
                counts[char_map.get(word[left], 5)] -= 1
                left += 1

            if all(c >= 1 for c in counts[:5]) and counts[-1] == k:
                res += 1

        while left < len(word):
            counts[char_map.get(word[left], 5)] -= 1
            left += 1
            if all(c >= 1 for c in counts[:5]) and counts[-1] == k:
                res += 1

        return res
