# 10. Regular Expression Matching

**Difficulty:** Hard  
**Language:** Python

## Problem

Given a string `s` and a pattern `p`, implement regular expression matching with support for `.` and `*`.

The character `.` matches any single character.

The character `*` matches zero or more of the preceding element.

The entire string must match the pattern.

## Example 1

### Input

s = "aa"  
p = "a"

### Output

false

## Example 2

### Input

s = "aa"  
p = "a*"

### Output

true

## Example 3

### Input

s = "ab"  
p = ".*"

### Output

true

## Approach

I use dynamic programming to determine whether different parts of the string match different parts of the pattern.

For each position in the string and pattern, I check whether the current characters match.

If the current pattern character is `*`, there are two possibilities:

- Ignore the `*` and the preceding character.
- Use the `*` to match the current character and continue matching.

The dynamic programming table stores the results of previously solved subproblems.

## Complexity

- Time Complexity: O(m × n)
- Space Complexity: O(m × n)

Where `m` is the length of the string and `n` is the length of the pattern.

## Solution

[View Solution](solution.py)
