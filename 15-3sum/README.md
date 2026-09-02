# 3Sum

## Problem

You are given an integer array `nums`.

Find all unique triplets `[nums[i], nums[j], nums[k]]` such that:

`nums[i] + nums[j] + nums[k] == 0`

The solution must not contain duplicate triplets.

### Example 1

**Input**

```text id="k8sh5m"
nums = [-1,0,1,2,-1,-4]
```

### Output

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/15-3sum/README.md#output)

```text
[[-1,-1,2],[-1,0,1]]
```

### Explanation

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/15-3sum/README.md#explanation)

The triplets that add up to `0` are:

```text
(-1) + (-1) + 2 = 0
(-1) + 0 + 1 = 0
```

Therefore, the distinct triplets are:

`[[-1,-1,2],[-1,0,1]]`

### Example 2

**Input**

```text id="b7e5nq"
nums = [0,1,1]
```

### Output

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/15-3sum/README.md#output)

```text
[]
```

### Explanation

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/15-3sum/README.md#explanation)

The only possible triplet is:

`0 + 1 + 1 = 2`

Since the sum is not `0`, there is no valid triplet.

Therefore, the answer is `[]`.

### Example 3

**Input**

```text id="r5h4td"
nums = [0,0,0]
```

### Output

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/15-3sum/README.md#output)

```text
[[0,0,0]]
```

### Explanation

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/15-3sum/README.md#explanation)

The only possible triplet is:

`0 + 0 + 0 = 0`

Therefore, the answer is `[[0,0,0]]`.

## Approach

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/15-3sum/README.md#approach)

I first sort the array.

Then, I use one fixed element and two pointers to find the other two elements.

The `left` pointer starts just after the fixed element and the `right` pointer starts at the end of the array.

If the sum of the three elements is `0`, I add the triplet to the result.

If the sum is less than `0`, I move the `left` pointer forward to increase the sum.

If the sum is greater than `0`, I move the `right` pointer backward to decrease the sum.

I also skip duplicate values to make sure that the result does not contain duplicate triplets.

## Complexity

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/15-3sum/README.md#complexity)

* Time Complexity: O(n²)
* Space Complexity: O(1) excluding the output

## Solution

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/15-3sum/README.md#solution)

[View Solution](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/15-3sum/solution.py)
