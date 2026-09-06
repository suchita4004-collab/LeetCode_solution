# 44. Wildcard Matching

## Problem

Given a string `s` and a pattern `p`, implement wildcard pattern matching.

The pattern supports two special characters:

- `?` matches any single character.
- `*` matches any sequence of characters, including an empty sequence.

The pattern must match the entire string.

## Example 1

Input:

`s = "aa"`
`p = "a"`

Output:

`False`

## Example 2

Input:

`s = "aa"`
`p = "*"`

Output:

`True`

## Example 3

Input:

`s = "cb"`
`p = "?a"`

Output:

`False`

## Approach

I use two pointers to scan the string and pattern.

The variables `i` and `j` represent the current positions in `s` and `p`.

There are three main cases:

1. If the current characters match, or the pattern contains `?`, move both pointers forward.
2. If the pattern contains `*`, store its position and move the pattern pointer forward.
3. If a mismatch occurs after seeing a `*`, let the `*` match one more character from the string and continue checking.

The `star` variable stores the most recent `*`, while `match` stores the position in the string where that `*` started matching.

At the end, any remaining characters in the pattern must be `*`.

## Complexity

- Time Complexity: O(m + n)
- Space Complexity: O(1)

where `m` is the length of `s` and `n` is the length of `p`.

## Solution

The complete Python solution is available in `solution.py`.
