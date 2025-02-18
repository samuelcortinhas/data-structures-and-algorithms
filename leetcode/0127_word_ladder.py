from collections import defaultdict, deque
from typing import List


class Solution:
    @staticmethod
    def connected(word1, word2):
        count = 0
        for c1, c2 in zip(word1, word2):
            if c1 != c2:
                count += 1
        return count == 1

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Time O(n^2 m), Memory O(n^2 * m) where n = len(wordList), m = len(endWord)

        # build graph where words are connected if they differ by 1 letter
        adj_list = defaultdict(list)
        wordList += [beginWord]
        for i1 in range(len(wordList)):
            for i2 in range(i1 + 1, len(wordList)):
                word1, word2 = wordList[i1], wordList[i2]
                if self.connected(word1, word2):
                    adj_list[word1].append(word2)
                    adj_list[word2].append(word1)

        # do bfs on this graph
        queue = deque()
        queue.append(beginWord)
        visit = set()
        res = 0
        while queue:
            res += 1
            for _ in range(len(queue)):
                curr_word = queue.popleft()
                if curr_word == endWord:
                    return res
                visit.add(curr_word)

                for neigh in adj_list[curr_word]:
                    if neigh not in visit:
                        queue.append(neigh)
        return 0
