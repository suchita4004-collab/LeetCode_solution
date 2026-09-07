# 0055 - Jump Game

## Problem

You are given an integer array `nums`.

You are initially positioned at the **first index** of the array.

Each element `nums[i]` represents the **maximum jump length** from that position.

From index `i`, you can jump to any index from:

```text
i + 1
```

up to:

```text
i + nums[i]
```

Return `true` if you can reach the last index. Otherwise, return `false`.

## Examples

### Example 1

Input:

```text
nums = [2,3,1,1,4]
```

Output:

```text
true
```

Explanation:

From index `0`, we can jump to index `1`.

Then from index `1`, we can jump `3` positions to the last index.

```text
0 → 1 → 4
```

Therefore, the answer is `true`.

### Example 2

Input:

```text
nums = [3,2,1,0,4]
```

Output:

```text
false
```

Explanation:

We can reach index `3`, but:

```text
nums[3] = 0
```

So we cannot move forward to index `4`.

Therefore, the answer is `false`.

## Approach

We use a **Greedy Algorithm**.

The main idea is to keep track of the **farthest index** that we can reach.

We maintain:

```text
farthest
```

which represents the maximum index reachable so far.

For every index `i`, we calculate:

```text
i + nums[i]
```

and update:

```text
farthest = max(farthest, i + nums[i])
```

If at any point:

```text
i > farthest
```

it means we cannot even reach the current index.

Therefore, reaching the last index is impossible.

## Algorithm

1. Initialize `farthest = 0`.
2. Traverse the array from left to right.
3. If the current index is greater than `farthest`, return `False`.
4. Update the farthest reachable position.
5. If `farthest` reaches the last index, return `True`.
6. If the loop finishes, return `True`.

## Solution

```python
class Solution:
    def canJump(self, nums):
        farthest = 0

        for i in range(len(nums)):
            if i > farthest:
                return False

            farthest = max(farthest, i + nums[i])

            if farthest >= len(nums) - 1:
                return True

        return True
```

## Dry Run

Consider:

```text
nums = [2,3,1,1,4]
```

Initially:

```text
farthest = 0
```

### Index 0

```text
nums[0] = 2
```

We can reach:

```text
0 + 2 = 2
```

So:

```text
farthest = 2
```

### Index 1

Index `1` is reachable.

```text
nums[1] = 3
```

We can reach:

```text
1 + 3 = 4
```

Update:

```text
farthest = 4
```

Since index `4` is the last index:

```text
farthest >= len(nums) - 1
```

Therefore:

```text
Output = true
```

## Dry Run for False Case

Consider:

```text
nums = [3,2,1,0,4]
```

Initially:

```text
farthest = 0
```

At index `0`:

```text
farthest = max(0, 0 + 3)
         = 3
```

At index `1`:

```text
farthest = max(3, 1 + 2)
         = 3
```

At index `2`:

```text
farthest = max(3, 2 + 1)
         = 3
```

At index `3`:

```text
nums[3] = 0
```

So:

```text
farthest = 3
```

Index `4` cannot be reached.

When `i = 4`:

```text
i > farthest
4 > 3
```

Therefore:

```text
Output = false
```

## Why Greedy Approach?

We do not need to try every possible jump.

Instead, we only need to know the **farthest position we can reach**.

If we can keep extending `farthest` until it reaches the last index, the answer is `true`.

If we encounter an index beyond `farthest`, that index cannot be reached, so the answer is `false`.

This makes the solution much more efficient than using recursion or dynamic programming.

## Complexity

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`

The array is traversed only once and only one extra variable is used.

## Key Concept

The main concept used in this problem is the **Greedy Algorithm**.

The important formula is:

```python
farthest = max(farthest, i + nums[i])
```

It keeps track of the maximum position that can be reached from the starting point.

## Constraints

- `1 <= nums.length <= 10^4`
- `0 <= nums[i] <= 10^5`

## Language

Python

## LeetCode Problem

Problem Number: **55**

Problem Name: **Jump Game**

Difficulty: **Medium**
