from typing import List


class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string."""
        # Time O(n), Memory O(n)
        return "".join([f"{len(s)}#{s}" for s in strs])

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings."""
        # Time O(n), Memory O(n)
        i = 0
        num = ""
        res = []
        while i < len(s):
            if s[i] == "#":
                res.append(s[i + 1 : i + 1 + int(num)])
                i += int(num) + 1
                num = ""
            else:
                num += s[i]
                i += 1
        return res


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
