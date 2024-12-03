from typing import List


class Solution:
    def encode(self, strs: List[str]) -> str:
        # Time O(n), Memory O(n)
        lens = [len(s) for s in strs]
        out = ""
        for x in strs:
            out = out + "{}#".format(len(x)) + x
        return out

    def decode(self, s: str) -> List[str]:
        # Time O(n), Memory O(n)
        i = 0
        out = []
        num = ""
        while i < len(s):
            if s[i] == "#":
                n = int(num)
                out.append(s[i + 1 : i + 1 + n])
                i = i + 1 + n
                num = ""
                continue

            num = num + s[i]
            i += 1
        return out
