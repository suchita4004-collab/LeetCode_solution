# 6. Zigzag Conversion

**Difficulty:** Medium  
**Language:** Python

## Problem

Given a string `s` and an integer `numRows`, arrange the characters in a
zigzag pattern and then read the characters row by row.

## Example 1

### Input

s = "PAYPALISHIRING"  
numRows = 3

### Output

"PAHNAPLSIIGYIR"

## Example 2

### Input

s = "PAYPALISHIRING"  
numRows = 4

### Output

"PINALSIGYAHRPI"

## Example 3

### Input

s = "A"  
numRows = 1

### Output

"A"

## Approach

I create a list for each row and move through the string character by
character.

The row position moves downward until it reaches the last row, then moves
upward until it reaches the first row.

This creates the zigzag pattern.

Finally, I join all rows together to produce the converted string.

## Complexity

- Time Complexity: O(n)
- Space Complexity: O(n)

## Solution

[View Solution](solution.py)
