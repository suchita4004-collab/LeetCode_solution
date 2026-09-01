# 3. Longest Substring Without Repeating Characters

**Difficulty:** Medium  
**Language:** Python

## Problem

Given a string `s`, find the length of the longest substring without duplicate characters.

## Example 1

### Input

s = "abcabcbb"

### Output

3

### Explanation

The longest substring without repeating characters is `"abc"`.

Its length is 3.

## Example 2

### Input

s = "bbbbb"

### Output

1

### Explanation

The longest substring without repeating characters is `"b"`.

Its length is 1.

## Example 3

### Input

s = "pwwkew"

### Output

3

### Explanation

The longest substring without repeating characters is `"wke"`.

Its length is 3.

## Approach

I use the sliding window technique with a set to keep track of characters in the current substring.

I maintain two pointers, `left` and `right`.

The `right` pointer expands the window by adding characters.

If a duplicate character is found, I remove characters from the left until the duplicate is removed.

For every valid window, I calculate its length and keep track of the maximum length.

## Complexity

- Time Complexity: O(n)
- Space Complexity: O(n)

## Solution

[View Solution](solution.py)
