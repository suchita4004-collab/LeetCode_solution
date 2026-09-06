# 42. Trapping Rain Water

## Problem

Given an array of non-negative integers representing an elevation map, where the width of each bar is 1, calculate how much rain water can be trapped after raining.

## Example 1

Input:

`height = [0,1,0,2,1,0,1,3,2,1,2,1]`

Output:

`6`

## Example 2

Input:

`height = [4,2,0,3,2,5]`

Output:

`9`

## Approach

I use the two-pointer approach.

I maintain two pointers:

- `left` starts from the beginning.
- `right` starts from the end.

I also keep track of:

- `left_max` - maximum height seen from the left.
- `right_max` - maximum height seen from the right.

At each step, I compare the heights at the left and right pointers.

If the left height is smaller or equal, I process the left side. Otherwise, I process the right side.

If the current height is smaller than the maximum height on that side, water can be trapped. The trapped water is calculated as:

`maximum height - current height`

The pointers are then moved toward each other.

## Complexity

- Time Complexity: O(n)
- Space Complexity: O(1)

## Solution

The complete Python solution is available in `solution.py`.
