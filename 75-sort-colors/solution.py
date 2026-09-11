```python id="p4k8mz"
class Solution:
    def sortColors(self, nums):
        low = 0
        mid = 0
        high = len(nums) - 1

        while mid <= high:

            # 0 should go to the beginning
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1

            # 1 stays in the middle
            elif nums[mid] == 1:
                mid += 1

            # 2 should go to the end
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
```
