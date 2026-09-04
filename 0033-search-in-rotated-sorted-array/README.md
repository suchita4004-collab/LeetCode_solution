# Search in Rotated Sorted Array

## Problem

You are given an integer array `nums` that was originally sorted in ascending order with distinct values.

The array may have been rotated at an unknown position.

For example:

```text id="z3u5x1"
[0,1,2,4,5,6,7]
```

After rotation, it can become:

```text id="k8n4rm"
[4,5,6,7,0,1,2]
```

Given the rotated array and a `target`, return the index of the target if it exists.

If the target is not present, return `-1`.

The algorithm must have **O(log n)** runtime complexity.

## Example 1

**Input**

```text id="a7s4cx"
nums = [4,5,6,7,0,1,2]
target = 0
```

### Output

```text id="j5x8q2"
4
```

### Explanation

The target `0` is present at index `4`.

## Example 2

**Input**

```text id="p9r3kd"
nums = [4,5,6,7,0,1,2]
target = 3
```

### Output

```text id="v2m6hw"
-1
```

### Explanation

The target `3` is not present in the array.

## Example 3

**Input**

```text id="n7c1fz"
nums = [1]
target = 0
```

### Output

```text id="b4q9tx"
-1
```

### Explanation

The array contains only `1`, so the target `0` is not found.

## Approach

I use **Binary Search** to search for the target in O(log n) time.

In a rotated sorted array, at least one half of the current search range is always sorted.

For each step:

1. Find the middle index.
2. If `nums[mid]` is equal to the target, return `mid`.
3. Check which half is sorted.
4. If the left half is sorted, check whether the target lies inside that range.
5. Otherwise, search in the other half.
6. If the right half is sorted, check whether the target lies inside that range.
7. Continue until the target is found or the search range becomes empty.

This allows us to eliminate half of the remaining elements at every step.

## Complexity

- **Time Complexity:** O(log n)
- **Space Complexity:** O(1)

The search is performed using binary search and no extra data structure is used.

## Solution

[View Solution](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/0033-search-in-rotated-sorted-array/solution.py)

## Folder Structure

```text id="t2w7kp"
0033-search-in-rotated-sorted-array/
├── README.md
└── solution.py
```
