class Solution:
    def lengthOfLongestSubstring(self, s):
        seen = set()
        left = 0
        maximum = 0

        for right in range(len(s)):
            # Remove characters until there is no duplicate
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])

            # Current window length
            length = right - left + 1

            if length > maximum:
                maximum = length

        return maximum
