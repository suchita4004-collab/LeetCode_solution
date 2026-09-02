# Container With Most Water

## Problem

You are given an integer array `height` where `height[i]` represents the height of a vertical line.

Find two lines that together with the x-axis form a container that can store the maximum amount of water.

### Example 1

**Input**

```text
height = [1,8,6,2,5,4,8,3,7]
```

### Output

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/11-container-with-most-water/README.md#output)

49

### Explanation

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/11-container-with-most-water/README.md#explanation)

The maximum amount of water that can be stored is `49`.

The two lines with heights `8` and `7` form the container.

The width between them is `7` and the smaller height is `7`.

Therefore, the maximum area is:

`7 × 7 = 49`

### Example 2

**Input**

```text
height = [1,1]
```

### Output

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/11-container-with-most-water/README.md#output)

1

### Explanation

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/11-container-with-most-water/README.md#explanation)

There are two lines with height `1`.

The width between them is `1`.

Therefore, the maximum amount of water is:

`1 × 1 = 1`

## Approach

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/11-container-with-most-water/README.md#approach)

I use the two-pointer approach.

I place one pointer at the beginning of the array and another pointer at the end.

For each pair of lines, I calculate the area using:

`area = min(height[left], height[right]) × (right - left)`

I keep track of the maximum area found.

If the left line is shorter, I move the left pointer forward.

Otherwise, I move the right pointer backward.

This helps to find the maximum area efficiently without checking every possible pair of lines.

## Complexity

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/11-container-with-most-water/README.md#complexity)

* Time Complexity: O(n)
* Space Complexity: O(1)

## Solution

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/11-container-with-most-water/README.md#solution)

[View Solution](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/11-container-with-most-water/solution.py)
