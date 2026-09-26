class Solution:
    def reverseWords(self, s):
        words = s.split()
        words.reverse()
        return " ".join(words)