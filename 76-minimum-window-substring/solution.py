```python
class Solution:
    def minWindow(self, s, t):
        if len(t) > len(s):
            return ""

        # Count required characters from t
        need = {}
        for char in t:
            need[char] = need.get(char, 0) + 1

        window = {}

        left = 0
        formed = 0
        required = len(need)

        min_length = float("inf")
        min_left = 0

        for right in range(len(s)):
            char = s[right]

            # Add current character to the window
            window[char] = window.get(char, 0) + 1

            # Character requirement is completely satisfied
            if char in need and window[char] == need[char]:
                formed += 1

            # Try to shrink the window
            while formed == required:
                window_length = right - left + 1

                if window_length < min_length:
                    min_length = window_length
                    min_left = left

                left_char = s[left]
                window[left_char] -= 1

                # Removing this character makes the window invalid
                if left_char in need and window[left_char] < need[left_char]:
                    formed -= 1

                left += 1

        if min_length == float("inf"):
            return ""

        return s[min_left:min_left + min_length]
```
