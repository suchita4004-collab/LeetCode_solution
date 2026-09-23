from collections import defaultdict

class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        word_set = set(wordList)

        if endWord not in word_set:
            return []

        # Stores all parents that can reach a word
        parents = defaultdict(list)

        # BFS
        current_level = {beginWord}
        found = False

        while current_level and not found:
            # Remove words already processed at the previous level
            word_set -= current_level

            next_level = set()

            for word in current_level:
                for i in range(len(word)):
                    for ch in "abcdefghijklmnopqrstuvwxyz":
                        if ch == word[i]:
                            continue

                        new_word = word[:i] + ch + word[i + 1:]

                        if new_word in word_set:
                            next_level.add(new_word)
                            parents[new_word].append(word)

                            if new_word == endWord:
                                found = True

            current_level = next_level

        if not found:
            return []

        # Backtrack from endWord to beginWord
        result = []
        path = [endWord]

        def backtrack(word):
            if word == beginWord:
                result.append(path[::-1])
                return

            for parent in parents[word]:
                path.append(parent)
                backtrack(parent)
                path.pop()

        backtrack(endWord)

        return result