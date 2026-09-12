```python
class Solution:
    def largestRectangleArea(self, heights):
        stack = []
        max_area = 0

        # Add a 0 at the end to process all remaining bars
        heights.append(0)

        for i, height in enumerate(heights):

            # Remove bars that are taller than the current bar
            while stack and heights[stack[-1]] > height:
                h = heights[stack.pop()]

                # Calculate the width of the rectangle
                if stack:
                    width = i - stack[-1] - 1
                else:
                    width = i

                # Calculate area
                area = h * width
                max_area = max(max_area, area)

            stack.append(i)

        # Remove the added 0
        heights.pop()

        return max_area
```
