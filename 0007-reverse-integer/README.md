# 7. Reverse Integer

**Difficulty:** Medium  
**Language:** Python

## Problem

Given a signed 32-bit integer `x`, return the integer with its digits
reversed.

If reversing the integer causes the result to go outside the signed
32-bit integer range `[-2³¹, 2³¹ - 1]`, return `0`.

## Example 1

### Input

x = 123

### Output

321

## Example 2

### Input

x = -123

### Output

-321

## Example 3

### Input

x = 120

### Output

21

## Approach

I reverse the digits of the integer and preserve its sign.

After reversing the number, I check whether the result is within the
signed 32-bit integer range.

The valid range is:

- Minimum: `-2³¹`
- Maximum: `2³¹ - 1`

If the reversed number is outside this range, I return `0`.

## Complexity

- Time Complexity: O(log n)
- Space Complexity: O(1)

## Solution

[View Solution](solution.py)
