# Remove Duplicates from Sorted Array

## Problem

Given an integer array `nums` sorted in non-decreasing order, remove the duplicates in-place so that each unique element appears only once.

The relative order of the elements should remain the same.

Return the number of unique elements `k`.

The first `k` elements of `nums` should contain the unique numbers in sorted order.

## Example 1

**Input**

```text
nums = [1,1,2]
```

### Output

```text
2
```

`nums` becomes:

```text
[1,2,_]
```

### Explanation

The unique elements are `1` and `2`.

Therefore, `k = 2`.

The elements after the first `k` positions can be ignored.

## Example 2

**Input**

```text
nums = [0,0,1,1,1,2,2,3,3,4]
```

### Output

```text
5
```

`nums` becomes:

```text
[0,1,2,3,4,_,_,_,_,_]
```

### Explanation

The unique elements are:

```text
0, 1, 2, 3, 4
```

Therefore, `k = 5`.

## Approach

I use the **two-pointer technique**.

Since the array is already sorted, duplicate elements are next to each other.

I keep a pointer `k` to indicate the position where the next unique element should be placed.

I start `k` from `1` because the first element is always unique.

Then I compare every element with the previous element:

- If they are different, the element is unique.
- I place the unique element at index `k`.
- Then I increase `k`.

At the end, `k` represents the total number of unique elements.

## Complexity

- Time Complexity: O(n)
- Space Complexity: O(1)

## Solution

[View Solution](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/26-remove-duplicates-from-sorted-array/solution.py)

## Folder Structure

```text
26-remove-duplicates-from-sorted-array/
├── README.md
└── solution.py
```
