````markdown
# 4Sum

Given an array of integers `nums` and an integer `target`, return all unique quadruplets `[nums[a], nums[b], nums[c], nums[d]]` such that their sum is equal to `target`.

The four indices must be distinct.

## Example 1

```text
Input: nums = [1,0,-1,0,-2,2], target = 0

Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
````

### Explanation

The unique quadruplets whose sum is `0` are:

* `-2 + (-1) + 1 + 2 = 0`
* `-2 + 0 + 0 + 2 = 0`
* `-1 + 0 + 0 + 1 = 0`

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/18-4sum/README.md#example-1)

## Example 2

```text
Input: nums = [2,2,2,2,2], target = 8

Output: [[2,2,2,2]]
```

### Explanation

The only unique quadruplet is `[2,2,2,2]` because:

`2 + 2 + 2 + 2 = 8`

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/18-4sum/README.md#example-2)

## Approach

1. First, sort the array.
2. Use two loops to fix the first two numbers.
3. Use two pointers, `left` and `right`, to find the remaining two numbers.
4. If the sum is equal to the target, add the quadruplet to the result.
5. If the sum is smaller than the target, move `left` forward.
6. If the sum is greater than the target, move `right` backward.
7. Skip duplicate values to make sure only unique quadruplets are added.

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/18-4sum/README.md#approach)

## Complexity

* **Time Complexity:** O(n³)
* **Space Complexity:** O(1), excluding the output array

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/18-4sum/README.md#complexity)

## Solution

[View Solution](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/18-4sum/solution.py)

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/18-4sum/README.md#solution)

## Folder Structure

```text
18-4sum/
├── README.md
└── solution.py
```

```
```
