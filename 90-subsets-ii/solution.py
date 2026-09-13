```python
class Solution:
    def subsetsWithDup(self, nums):
        nums.sort()

        result = []
        current = []

        def backtrack(start):
            # Add the current subset
            result.append(current[:])

            for i in range(start, len(nums)):

                # Skip duplicate elements at the same level
                if i > start and nums[i] == nums[i - 1]:
                    continue

                current.append(nums[i])

                # Generate subsets using the next elements
                backtrack(i + 1)

                # Remove the last element
                current.pop()

        backtrack(0)

        return result
```
