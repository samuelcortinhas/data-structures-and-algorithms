from typing import List


# Idea: store words in a prefix tree. DFS on grid.
class TrieNode:
    def __init__(self):
        # Memory O(N*W) where N=#words, W=max word len
        self.children = {}
        self.is_word = False

    def add_word(self, word):
        # Time O(W)
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.is_word = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Time O(m*n*4^(m*n) + N*W), Memory O(m*n + N*W)
        m, n = len(board), len(board[0])
        root = TrieNode()
        for word in words:
            root.add_word(word)
        res, seen = set(), set()

        def dfs(i, j, node, curr):
            if (
                i < 0
                or j < 0
                or i >= m
                or j >= n
                or (i, j) in seen
                or board[i][j] not in node.children
            ):
                return

            seen.add((i, j))
            curr += board[i][j]
            child = node.children[board[i][j]]
            if child.word:
                res.add(curr)

            dfs(i + 1, j, child, curr)
            dfs(i - 1, j, child, curr)
            dfs(i, j + 1, child, curr)
            dfs(i, j - 1, child, curr)

            curr = curr[:-1]
            seen.remove((i, j))

        for i in range(m):
            for j in range(n):
                dfs(i, j, root, "")

        return list(res)


# This took me 25 mins first try having never seen it before! (essentially problems 79 + 208)
