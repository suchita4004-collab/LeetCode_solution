```python id="f6y3n8"
class Solution:
    def removeDuplicates(self, nums):
        # If there are 2 or fewer elements,
        # no changes are needed
        if len(nums) <= 2:
            return len(nums)

        # Position where the next valid element will be placed
        write = 2

        # Start checking from the third element
        for read in range(2, len(nums)):

            # Allow the current number only if it is
            # different from the element two positions back
            if nums[read] != nums[write - 2]:
                nums[write] = nums[read]
                write += 1

        return write
```
