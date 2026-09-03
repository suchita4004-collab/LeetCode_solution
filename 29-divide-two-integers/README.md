# Divide Two Integers

## Problem

Given two integers `dividend` and `divisor`, divide the two integers without using multiplication, division, or modulo operators.

The result should be truncated toward zero.

For example:

```text
8.345 → 8
-2.7335 → -2
```

If the quotient is outside the 32-bit signed integer range, return the corresponding limit.

The 32-bit signed integer range is:

```text
[-2^31, 2^31 - 1]
```

## Example 1

**Input**

```text
dividend = 10
divisor = 3
```

### Output

```text
3
```

### Explanation

`10 / 3 = 3.33333...`

After truncating toward zero, the result is `3`.

## Example 2

**Input**

```text
dividend = 7
divisor = -3
```

### Output

```text
-2
```

### Explanation

`7 / -3 = -2.33333...`

After truncating toward zero, the result is `-2`.

## Approach

I use **repeated doubling** instead of multiplication or division.

First, I determine whether the result should be positive or negative.

Then I convert both numbers to positive values using `abs()`.

For each step:

1. Start with the divisor and a multiple of `1`.
2. Double the divisor and multiple while the doubled value is not greater than the dividend.
3. Subtract the largest possible doubled value from the dividend.
4. Add the corresponding multiple to the quotient.
5. Continue until the remaining dividend is smaller than the divisor.

Finally, I apply the correct sign to the quotient.

I also check the 32-bit integer limits before returning the result.

## Complexity

- **Time Complexity:** O(log n)
- **Space Complexity:** O(1)

## Solution

[View Solution](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/29-divide-two-integers/solution.py)

## Folder Structure

```text
29-divide-two-integers/
├── README.md
└── solution.py
```
