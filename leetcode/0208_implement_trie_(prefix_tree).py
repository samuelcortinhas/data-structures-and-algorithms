class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False


class Trie:
    def __init__(self):
        self.head = TrieNode()

    def insert(self, word: str) -> None:
        # Time O(n)
        curr = self.head
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.word = True

    def search(self, word: str) -> bool:
        # Time O(n)
        curr = self.head
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.word

    def startsWith(self, prefix: str) -> bool:
        # Time O(n)
        curr = self.head
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
