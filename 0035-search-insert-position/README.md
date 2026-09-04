# Search Insert Position

## Problem

Given a sorted array of distinct integers and a target value, return the index if the target is found.

If the target is not found, return the index where it should be inserted so that the array remains sorted.

The algorithm must have **O(log n)** runtime complexity.

## Example 1

**Input**

```text
nums = [1,3,5,6]
target = 5
```

### Output

```text
2
```

### Explanation

The target `5` is already present at index `2`.

## Example 2

**Input**

```text
nums = [1,3,5,6]
target = 2
```

### Output

```text
1
```

### Explanation

The target `2` is not present.

It should be inserted between `1` and `3`, so its correct index is `1`.

## Example 3

**Input**

```text
nums = [1,3,5,6]
target = 7
```

### Output

```text
4
```

### Explanation

The target `7` is greater than all elements, so it should be inserted at the end of the array.

Therefore, the correct index is `4`.

## Approach

I use **Binary Search** to find the target or its correct insertion position.

For every step:

1. Find the middle index.
2. If `nums[mid]` is equal to the target, return `mid`.
3. If `nums[mid]` is smaller than the target, search in the right half.
4. Otherwise, search in the left half.
5. When the search ends, `left` represents the correct position where the target should be inserted.

Therefore, I return `left`.

## Complexity

- **Time Complexity:** O(log n)
- **Space Complexity:** O(1)

Binary search eliminates half of the remaining elements at every step.

## Solution

[View Solution](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/0035-search-insert-position/solution.py)

## Folder Structure

```text
0035-search-insert-position/
├── README.md
└── solution.py
```
