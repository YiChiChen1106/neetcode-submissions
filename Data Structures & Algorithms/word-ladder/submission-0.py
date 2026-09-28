from collections import deque
from typing import List

class Solution:
    def ladderLength(
        self,
        beginWord: str,
        endWord: str,
        wordList: List[str]
    ) -> int:

        words = set(wordList)

        if endWord not in words:
            return 0

        q = deque([(beginWord, 1)])

        while q:
            word, length = q.popleft()

            if word == endWord:
                return length

            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":

                    new_word = word[:i] + c + word[i + 1:]

                    if new_word in words:
                        q.append((new_word, length + 1))

                        # 防止重复访问
                        words.remove(new_word)

        return 0

