# Find First and Last Position of Element in Sorted Array

## Problem

Given an array of integers `nums` sorted in non-decreasing order, find the starting and ending position of a given `target` value.

If the target is not found, return:

```text
[-1,-1]
```

The algorithm must have **O(log n)** runtime complexity.

## Example 1

**Input**

```text
nums = [5,7,7,8,8,10]
target = 8
```

### Output

```text
[3,4]
```

### Explanation

The target `8` appears at indices `3` and `4`.

Therefore, the starting position is `3` and the ending position is `4`.

## Example 2

**Input**

```text
nums = [5,7,7,8,8,10]
target = 6
```

### Output

```text
[-1,-1]
```

### Explanation

The target `6` is not present in the array.

## Example 3

**Input**

```text
nums = []
target = 0
```

### Output

```text
[-1,-1]
```

### Explanation

The array is empty, so the target cannot be found.

## Approach

I use **Binary Search** two times.

First, I find the **first occurrence** of the target.

When the target is found, I store its index and continue searching on the left side to check if the target occurs earlier.

Second, I find the **last occurrence** of the target.

When the target is found, I store its index and continue searching on the right side to check if the target occurs later.

Finally, I return both positions:

```text
[first position, last position]
```

If the target does not exist, both positions remain `-1`.

## Complexity

- **Time Complexity:** O(log n)
- **Space Complexity:** O(1)

Binary search is performed twice, and no extra data structure is used.

## Solution

[View Solution](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/0034-find-first-and-last-position-of-element-in-sorted-array/solution.py)

## Folder Structure

```text
0034-find-first-and-last-position-of-element-in-sorted-array/
├── README.md
└── solution.py
```
