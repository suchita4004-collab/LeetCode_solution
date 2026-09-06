# 47. Permutations II

## Problem

Given a collection of numbers `nums` that may contain duplicates, return all possible unique permutations.

The answer can be returned in any order.

## Example 1

Input:

`nums = [1,1,2]`

Output:

`[[1,1,2],[1,2,1],[2,1,1]]`

## Example 2

Input:

`nums = [1,2,3]`

Output:

`[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]`

## Approach

I use backtracking to generate all possible permutations.

First, I sort the array. Sorting places duplicate numbers next to each other, which makes it easier to avoid generating duplicate permutations.

I use:

- `path` to store the current permutation.
- `used` to keep track of the elements already selected.

To avoid duplicate permutations, I skip the current number when it is the same as the previous number and the previous number has not been used at the current recursion level.

The condition is:

`if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:`

When the length of `path` becomes equal to the length of `nums`, a complete unique permutation is added to the result.

## Complexity

- Time Complexity: O(n × n!)
- Space Complexity: O(n)

The result itself can require O(n × n!) space.

## Solution

The complete Python solution is available in `solution.py`.
