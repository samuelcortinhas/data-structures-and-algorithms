from collections import Counter, defaultdict


class Solution:
    @staticmethod
    def is_valid(counts1, counts2):
        for k, v in counts2.items():
            if counts1[k] < v:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        # Time O(s*t), Memory O(s+t)
        s_counts = defaultdict(int)
        t_counts = Counter(t)
        left, right = 0, 0
        res = s + "a"
        while right < len(s) + 1:
            if left < right and s_counts[s[left]] > t_counts[s[left]]:
                s_counts[s[left]] -= 1
                left += 1
            else:
                if right < len(s):
                    s_counts[s[right]] += 1
                right += 1
            if self.is_valid(s_counts, t_counts) and right - left < len(res):
                res = s[left:right]
        return res if len(res) <= len(s) else ""
