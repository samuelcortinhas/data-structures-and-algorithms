class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        counts1 = [0] * 26
        counts2 = [0] * 26

        for c in s1:
            counts1[ord(c) - ord("a")] += 1

        left, right = 0, len(s1) - 1
        for c in s2[left : right + 1]:
            counts2[ord(c) - ord("a")] += 1

        while True:
            if counts1 == counts2:
                return True

            left += 1
            right += 1

            if right == len(s2):
                break

            counts2[ord(s2[right]) - ord("a")] += 1
            counts2[ord(s2[left - 1]) - ord("a")] -= 1

        return False
