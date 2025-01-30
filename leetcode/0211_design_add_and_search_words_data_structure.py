class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True

    def search(self, word: str) -> bool:
        return self.dfs(word, self.root)

    def dfs(self, word, curr):
        for i, c in enumerate(word):
            if c == ".":
                if i == len(word) - 1:
                    for v in curr.children.values():
                        if v.word:
                            return True
                    return False

                for v in curr.children.values():
                    if self.dfs(word[i + 1 :], v):
                        return True
                return False

            elif c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.word


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
