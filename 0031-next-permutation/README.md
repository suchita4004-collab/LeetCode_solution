# Next Permutation

## Problem

A permutation of an array is an arrangement of its elements in a particular order.

The **next permutation** is the next lexicographically greater arrangement of the array.

If no greater permutation is possible, the array should be rearranged into the lowest possible order, which means sorting it in ascending order.

The solution must modify the array **in-place** and use only constant extra memory.

## Example 1

**Input**

```text
nums = [1,2,3]
```

### Output

```text
[1,3,2]
```

### Explanation

The next permutation after `[1,2,3]` is `[1,3,2]`.

## Example 2

**Input**

```text
nums = [3,2,1]
```

### Output

```text
[1,2,3]
```

### Explanation

`[3,2,1]` is already the largest possible permutation.

Therefore, we rearrange it into the smallest permutation `[1,2,3]`.

## Example 3

**Input**

```text
nums = [1,1,5]
```

### Output

```text
[1,5,1]
```

### Explanation

The next lexicographically greater permutation is `[1,5,1]`.

## Approach

I use the following steps to find the next permutation:

1. Start from the right side and find the first index `i` such that:

```text
nums[i] < nums[i + 1]
```

This is the position where we can make the permutation larger.

2. If such an index exists, find an element from the right side that is greater than `nums[i]`.

3. Swap `nums[i]` with that element.

4. Reverse the part of the array after index `i`.

The suffix was originally in decreasing order, so reversing it makes it the smallest possible suffix.

If no such `i` exists, the entire array is in decreasing order. In that case, simply reverse the complete array to get the smallest permutation.

## Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

The array is modified in-place and no extra array is used.

## Solution

[View Solution](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/0031-next-permutation/solution.py)

## Folder Structure

```text
0031-next-permutation/
├── README.md
└── solution.py
```
