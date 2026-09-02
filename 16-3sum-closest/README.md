# 3Sum Closest

## Problem

You are given an integer array `nums` and an integer `target`.

Find three integers at distinct indices in `nums` such that their sum is closest to `target`.

Return the sum of the three integers.

### Example 1

**Input**

```text
nums = [-1,2,1,-4]
target = 1
```

### Output

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/16-3sum-closest/README.md#output)

2

### Explanation

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/16-3sum-closest/README.md#explanation)

The sum closest to the target is `2`.

```text
-1 + 2 + 1 = 2
```

The difference from the target is:

`|2 - 1| = 1`

Therefore, the answer is `2`.

### Example 2

**Input**

```text
nums = [0,0,0]
target = 1
```

### Output

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/16-3sum-closest/README.md#output)

0

### Explanation

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/16-3sum-closest/README.md#explanation)

The only possible sum is:

`0 + 0 + 0 = 0`

The difference from the target is:

`|0 - 1| = 1`

Therefore, the answer is `0`.

## Approach

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/16-3sum-closest/README.md#approach)

I first sort the array.

Then, I use one fixed element and two pointers to find the sum of three numbers.

The `left` pointer starts after the fixed element and the `right` pointer starts at the end of the array.

For every combination, I calculate the current sum and compare its difference from the target with the closest sum found so far.

If the current sum is smaller than the target, I move the `left` pointer forward.

If the current sum is greater than the target, I move the `right` pointer backward.

If the current sum is exactly equal to the target, I return it because it is the closest possible sum.

## Complexity

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/16-3sum-closest/README.md#complexity)

* Time Complexity: O(n²)
* Space Complexity: O(1) excluding the sorting space

## Solution

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/16-3sum-closest/README.md#solution)

[View Solution](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/16-3sum-closest/solution.py)
