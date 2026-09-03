# Remove Element

## Problem

Given an integer array `nums` and an integer `val`, remove all occurrences of `val` from `nums` in-place.

The order of the remaining elements may be changed.

Return the number of elements in `nums` which are not equal to `val`.

Let this number be `k`.

After removing the elements:

- The first `k` elements of `nums` should contain the elements that are not equal to `val`.
- The elements after index `k - 1` can be ignored.
- Return `k`.

## Example 1

**Input**

```text
nums = [3,2,2,3]
val = 3
```

### Output

```text
2
```

`nums` becomes:

```text
[2,2,_,_]
```

### Explanation

The value `3` occurs twice, so both occurrences are removed.

The remaining elements are `2` and `2`.

Therefore, `k = 2`.

## Example 2

**Input**

```text
nums = [0,1,2,2,3,0,4,2]
val = 2
```

### Output

```text
5
```

`nums` can become:

```text
[0,1,3,0,4,_,_,_]
```

### Explanation

All occurrences of `2` are removed.

The remaining elements are:

```text
0, 1, 3, 0, 4
```

Therefore, `k = 5`.

The order of these elements does not matter.

## Approach

I use a **two-pointer technique**.

I keep a pointer `k` that represents the position where the next element that is not equal to `val` should be placed.

I iterate through the array using pointer `i`.

- If `nums[i]` is not equal to `val`, I copy it to `nums[k]`.
- Then I increase `k`.
- If `nums[i]` is equal to `val`, I skip it.

At the end, `k` contains the number of elements that are not equal to `val`.

## Complexity

- Time Complexity: O(n)
- Space Complexity: O(1)

## Solution

[View Solution](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/27-remove-element/solution.py)

## Folder Structure

```text
27-remove-element/
├── README.md
└── solution.py
```
