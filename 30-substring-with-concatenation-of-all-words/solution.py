class Solution:
    def findSubstring(self, s, words):
        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count

        if total_len > len(s):
            return []

        word_freq = {}

        for word in words:
            word_freq[word] = word_freq.get(word, 0) + 1

        result = []

        for offset in range(word_len):
            left = offset
            right = offset
            current_count = 0
            current_freq = {}

            while right + word_len <= len(s):
                word = s[right:right + word_len]
                right += word_len

                if word not in word_freq:
                    current_freq = {}
                    current_count = 0
                    left = right
                    continue

                current_freq[word] = current_freq.get(word, 0) + 1
                current_count += 1

                while current_freq[word] > word_freq[word]:
                    left_word = s[left:left + word_len]
                    current_freq[left_word] -= 1
                    left += word_len
                    current_count -= 1

                if current_count == word_count:
                    result.append(left)

                    left_word = s[left:left + word_len]
                    current_freq[left_word] -= 1
                    left += word_len
                    current_count -= 1

        return result
