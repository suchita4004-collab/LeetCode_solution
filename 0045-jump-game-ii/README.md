# 45. Jump Game II

## Problem

Given a 0-indexed array `nums`, you are initially positioned at index `0`.

Each element `nums[i]` represents the maximum number of steps that can be jumped forward from index `i`.

Return the minimum number of jumps required to reach the last index.

It is guaranteed that the last index can be reached.

## Example 1

Input:

`nums = [2,3,1,1,4]`

Output:

`2`

### Explanation

Jump from index `0` to index `1`.

Then jump from index `1` to index `4`.

Therefore, the minimum number of jumps is `2`.

## Example 2

Input:

`nums = [2,3,0,1,4]`

Output:

`2`

## Approach

I use a Greedy approach.

I keep track of three variables:

- `jumps` - number of jumps made so far.
- `current_end` - the farthest index that can be reached using the current number of jumps.
- `farthest` - the farthest index that can be reached from the current range.

For every index, I update `farthest` using:

`i + nums[i]`

When the current index reaches `current_end`, I have to make another jump. I then update `current_end` to `farthest`.

I stop at `len(nums) - 1` because no jump is needed after reaching the last index.

## Complexity

- Time Complexity: O(n)
- Space Complexity: O(1)

## Solution

The complete Python solution is available in `solution.py`.
