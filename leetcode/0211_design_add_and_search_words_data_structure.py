class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False


class WordDictionary:
    def __init__(self):
        # Memory O(n*w) where n=#words, w=avg len(word)
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        # Time O(w)
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True

    def search(self, word: str) -> bool:
        # Time O(w * 26^2)
        def dfs(curr, index):
            if index == len(word):
                return curr.word

            if word[index] == ".":
                for v in curr.children.values():
                    if dfs(v, index + 1):
                        return True

            if word[index] in curr.children:
                return dfs(curr.children[word[index]], index + 1)

            return False

        return dfs(self.root, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
