# 39. Combination Sum

## Problem

Given an array of distinct integers `candidates` and a target integer `target`, return all unique combinations of `candidates` where the chosen numbers add up to `target`.

The same number can be chosen an unlimited number of times.

Two combinations are considered unique if at least one number is used a different number of times.

## Example 1

**Input:** `candidates = [2,3,6,7]`, `target = 7`

**Output:** `[[2,2,3],[7]]`

### Explanation

`2 + 2 + 3 = 7`

and

`7 = 7`

These are the only possible combinations.

## Example 2

**Input:** `candidates = [2,3,5]`, `target = 8`

**Output:** `[[2,2,2,2],[2,3,3],[3,5]]`

## Example 3

**Input:** `candidates = [2]`, `target = 1`

**Output:** `[]`

## Approach

I use **backtracking** to find all possible combinations.

For each candidate, I have two choices:

1. Choose the current candidate and continue using it because the same number can be used multiple times.
2. Skip the current candidate and move to the next candidate.

If the remaining target becomes `0`, the current combination is added to the result.

If the remaining target becomes negative, that combination cannot be used.

I also start each recursive call from the current index so that the same combination is not generated in different orders.

## Complexity

- Time Complexity: O(2^target) approximately, depending on the candidates.
- Space Complexity: O(target)

The space is used by the recursion stack and the current combination.

## Solution

[View Solution](solution.py)
