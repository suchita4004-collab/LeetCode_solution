# 9. Palindrome Number

**Difficulty:** Easy  
**Language:** Python

## Problem

Given an integer `x`, return `true` if `x` is a palindrome and `false` otherwise.

A palindrome is a number that reads the same from left to right and from right to left.

## Example 1

### Input

x = 121

### Output

true

## Example 2

### Input

x = -121

### Output

false

## Example 3

### Input

x = 10

### Output

false

## Approach

I check whether the integer reads the same forward and backward.

Negative numbers are not palindromes because the negative sign would appear at the opposite end when the number is reversed.

I reverse the digits of the number mathematically without converting the integer to a string.

Finally, I compare the reversed number with the original number.

If both numbers are equal, the number is a palindrome.

## Complexity

- Time Complexity: O(log n)
- Space Complexity: O(1)

## Solution

[View Solution](solution.py)
