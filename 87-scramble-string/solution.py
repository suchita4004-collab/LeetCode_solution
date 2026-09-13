```python
class Solution:
    def isScramble(self, s1, s2):
        memo = {}

        def solve(a, b):
            # Same strings are always scrambled versions
            if a == b:
                return True

            # Different lengths cannot be scrambled
            if len(a) != len(b):
                return False

            key = (a, b)

            # Return already calculated result
            if key in memo:
                return memo[key]

            # Scrambled strings must contain the same characters
            if sorted(a) != sorted(b):
                memo[key] = False
                return False

            n = len(a)

            # Try every possible split
            for i in range(1, n):

                # Case 1: No swap
                if solve(a[:i], b[:i]) and solve(a[i:], b[i:]):
                    memo[key] = True
                    return True

                # Case 2: Swap
                if solve(a[:i], b[n-i:]) and solve(a[i:], b[:n-i]):
                    memo[key] = True
                    return True

            memo[key] = False
            return False

        return solve(s1, s2)
```
