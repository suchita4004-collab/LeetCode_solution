```python
class Solution:
    def restoreIpAddresses(self, s):
        result = []

        def backtrack(start, parts):
            # If 4 parts are formed
            if len(parts) == 4:
                # Use all digits
                if start == len(s):
                    result.append(".".join(parts))
                return

            # Remaining digits and parts
            remaining = len(s) - start
            needed = 4 - len(parts)

            # Not enough or too many digits left
            if remaining < needed or remaining > needed * 3:
                return

            # Each IP part can contain 1 to 3 digits
            for length in range(1, 4):
                if start + length > len(s):
                    break

                part = s[start:start + length]

                # Leading zero is not allowed
                if len(part) > 1 and part[0] == '0':
                    continue

                # Value must be between 0 and 255
                if int(part) > 255:
                    continue

                parts.append(part)
                backtrack(start + length, parts)
                parts.pop()

        backtrack(0, [])

        return result
``````python
class Solution:
    def restoreIpAddresses(self, s):
        result = []

        def backtrack(start, parts):
            # If 4 parts are formed
            if len(parts) == 4:
                # Use all digits
                if start == len(s):
                    result.append(".".join(parts))
                return

            # Remaining digits and parts
            remaining = len(s) - start
            needed = 4 - len(parts)

            # Not enough or too many digits left
            if remaining < needed or remaining > needed * 3:
                return

            # Each IP part can contain 1 to 3 digits
            for length in range(1, 4):
                if start + length > len(s):
                    break

                part = s[start:start + length]

                # Leading zero is not allowed
                if len(part) > 1 and part[0] == '0':
                    continue

                # Value must be between 0 and 255
                if int(part) > 255:
                    continue

                parts.append(part)
                backtrack(start + length, parts)
                parts.pop()

        backtrack(0, [])

        return result
```
