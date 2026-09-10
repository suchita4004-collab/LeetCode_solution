```python
class Solution:
    def mySqrt(self, x):
        if x < 2:
            return x

        left = 1
        right = x // 2
        answer = 0

        while left <= right:
            mid = (left + right) // 2

            if mid <= x // mid:
                answer = mid
                left = mid + 1
            else:
                right = mid - 1

        return answer
```
