# 46. Permutations

## Problem

Given an array `nums` containing distinct integers, return all possible permutations of the array.

The answer can be returned in any order.

## Example 1

Input:

`nums = [1,2,3]`

Output:

`[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]`

## Example 2

Input:

`nums = [0,1]`

Output:

`[[0,1],[1,0]]`

## Example 3

Input:

`nums = [1]`

Output:

`[[1]]`

## Approach

I use **backtracking** to generate all possible permutations.

I maintain:

- `path` - stores the current permutation.
- `used` - keeps track of which elements have already been selected.

At every step, I try every unused number and add it to the current path.

When the length of `path` becomes equal to the length of `nums`, a complete permutation is created and added to the result.

After returning from the recursive call, I remove the last element and mark it as unused. This allows the number to be used in another permutation.

## Complexity

There are `n!` possible permutations.

- Time Complexity: O(n × n!)
- Space Complexity: O(n)

The result itself requires O(n × n!) space to store all permutations.

## Solution

The complete Python solution is available in `solution.py`.
