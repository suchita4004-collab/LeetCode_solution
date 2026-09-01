# 4. Median of Two Sorted Arrays

**Difficulty:** Hard  
**Language:** Python

## Problem

Given two sorted arrays `nums1` and `nums2`, return the median of the two sorted arrays.

The solution should have a time complexity of `O(log(m + n))`.

## Example 1

### Input

nums1 = [1, 3]  
nums2 = [2]

### Output

2.00000

### Explanation

The combined sorted array is `[1, 2, 3]`.

The median is `2`.

## Example 2

### Input

nums1 = [1, 2]  
nums2 = [3, 4]

### Output

2.50000

### Explanation

The combined sorted array is `[1, 2, 3, 4]`.

The median is:

`(2 + 3) / 2 = 2.5`

## Approach

I use binary search to find the correct partition between the two sorted arrays.

The smaller array is used for the binary search to keep the number of operations efficient.

The arrays are divided into left and right parts such that every element on the left side is less than or equal to every element on the right side.

Once the correct partition is found, the median is calculated based on whether the total number of elements is odd or even.

## Complexity

- Time Complexity: O(log(min(m, n)))
- Space Complexity: O(1)

## Solution

[View Solution](solution.py)
