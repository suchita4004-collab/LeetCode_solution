# 8. String to Integer (atoi)

**Difficulty:** Medium  
**Language:** Python

## Problem

Implement the `myAtoi` function to convert a string into a 32-bit signed integer.

The function should:

1. Ignore leading whitespace.
2. Determine whether the number is positive or negative.
3. Read consecutive digits and convert them into an integer.
4. Stop reading when a non-digit character is found.
5. Keep the result within the 32-bit signed integer range.

The valid range is:

- Minimum: `-2³¹`
- Maximum: `2³¹ - 1`

## Examples

### Example 1

**Input:**Output:

42
Example 2

Input:

s = " -042"

Output:

-42
Example 3

Input:

s = "1337c0d3"

Output:

1337
Example 4

Input:

s = "0-1"

Output:

0
Example 5

Input:

s = "words and 987"

Output:

0
Approach

I first remove the leading whitespace and check whether the next character
is + or - to determine the sign.

Then I read the consecutive digit characters and build the number.

If a non-digit character is encountered, the conversion stops.

Finally, I check whether the result is outside the 32-bit signed integer
range. If it is too large, I return the appropriate boundary value.

Complexity
Time Complexity: O(n)
Space Complexity: O(1)
Solution

View Solution
