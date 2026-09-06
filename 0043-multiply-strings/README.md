# 43. Multiply Strings

## Problem

Given two non-negative integers `num1` and `num2` represented as strings, return their product as a string.

We cannot use a BigInteger library or directly convert the complete strings into integers.

## Example 1

Input:

`num1 = "2"`
`num2 = "3"`

Output:

`"6"`

## Example 2

Input:

`num1 = "123"`
`num2 = "456"`

Output:

`"56088"`

## Approach

I use an array to store the digits of the multiplication result.

The multiplication is performed digit by digit, similar to the multiplication method used by hand.

For every digit of `num1`, I multiply it with every digit of `num2`.

The result is stored at the appropriate positions in the result array.

After all multiplications are completed, I remove leading zeros and convert the digits into a string.

The complete numbers are never converted into an integer.

## Complexity

- Time Complexity: O(m × n)
- Space Complexity: O(m + n)

where `m` is the length of `num1` and `n` is the length of `num2`.

## Solution

The complete Python solution is available in `solution.py`.
