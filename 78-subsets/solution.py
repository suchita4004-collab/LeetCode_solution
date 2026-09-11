```python
class Solution:
    def subsets(self, nums):
        result = []
        current = []

        def backtrack(start):
            # Add the current subset
            result.append(current[:])

            # Generate subsets starting from the current index
            for i in range(start, len(nums)):
                current.append(nums[i])
                backtrack(i + 1)
                current.pop()

        backtrack(0)
        return result
```
