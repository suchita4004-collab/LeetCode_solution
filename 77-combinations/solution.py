```python
class Solution:
    def combine(self, n, k):
        result = []
        current = []

        def backtrack(start):
            # If k numbers are selected, store the combination
            if len(current) == k:
                result.append(current[:])
                return

            # Try every possible number
            for num in range(start, n + 1):
                current.append(num)

                # Choose the next number
                backtrack(num + 1)

                # Remove the number and try another choice
                current.pop()

        backtrack(1)

        return result
```
