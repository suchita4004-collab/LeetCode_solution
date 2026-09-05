# 41. First Missing Positive

## Problem

Given an unsorted integer array `nums`, return the smallest positive integer that is not present in the array.

The solution must run in `O(n)` time and use `O(1)` extra space.

## Example 1

**Input:** `nums = [1,2,0]`

**Output:** `3`

### Explanation

The positive numbers `1` and `2` are present in the array, so the smallest missing positive integer is `3`.

## Example 2

**Input:** `nums = [3,4,-1,1]`

**Output:** `2`

### Explanation

`1` is present in the array, but `2` is missing.

Therefore, the answer is `2`.

## Example 3

**Input:** `nums = [7,8,9,11,12]`

**Output:** `1`

### Explanation

The smallest positive integer `1` is not present in the array.

Therefore, the answer is `1`.

## Approach

I use the array itself to place each positive number at its correct index.

For a number `x`, its correct position is index `x - 1`.

I first rearrange the elements so that:

- `1` is at index `0`
- `2` is at index `1`
- `3` is at index `2`
- and so on.

I ignore numbers that are less than `1` or greater than the length of the array.

After rearranging, I check the array from the beginning. The first index where `nums[i] != i + 1` gives the smallest missing positive integer.

If every position contains the correct value, then the answer is `n + 1`.

## Complexity

- Time Complexity: O(n)
- Space Complexity: O(1)

The array is modified in-place and no extra data structure is used.

## Solution

[View Solution](solution.py)
