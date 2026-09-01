# 5. Longest Palindromic Substring

**Difficulty:** Medium  
**Language:** Python

## Problem

Given a string `s`, return the longest palindromic substring in `s`.

A palindrome is a string that reads the same forward and backward.

## Example 1

### Input

s = "babad"

### Output

"bab"

### Explanation

"bab" is a palindrome.  
"aba" is also a valid answer.

## Example 2

### Input

s = "cbbd"

### Output

"bb"

## Approach

I use the expand-around-center technique.

Every palindrome has a center. The center can be:

- A single character for odd-length palindromes.
- The space between two characters for even-length palindromes.

For each possible center, I expand outward while the characters are equal.

I keep track of the longest palindrome found.

## Complexity

- Time Complexity: O(n²)
- Space Complexity: O(1)

## Solution

[View Solution](solution.py)
