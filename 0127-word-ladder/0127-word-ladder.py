from collections import deque

class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        word_set = set(wordList)

        if endWord not in word_set:
            return 0

        queue = deque([(beginWord, 1)])

        while queue:
            word, steps = queue.popleft()

            if word == endWord:
                return steps

            for i in range(len(word)):
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    if ch == word[i]:
                        continue

                    new_word = word[:i] + ch + word[i + 1:]

                    if new_word in word_set:
                        word_set.remove(new_word)
                        queue.append((new_word, steps + 1))

        return 0
