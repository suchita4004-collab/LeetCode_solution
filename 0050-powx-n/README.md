# 0050 - Pow(x, n)

## Problem

Implement `pow(x, n)`, which calculates `x` raised to the power `n`.

In other words:

```text
x^n
```

The exponent `n` can be positive, zero, or negative.

You should implement the solution efficiently without using the built-in power function.

## Examples

### Example 1

Input:

```text
x = 2.00000
n = 10
```

Output:

```text
1024.00000
```

Explanation:

```text
2^10 = 1024
```

### Example 2

Input:

```text
x = 2.10000
n = 3
```

Output:

```text
9.26100
```

Explanation:

```text
2.1^3 = 2.1 × 2.1 × 2.1 = 9.261
```

### Example 3

Input:

```text
x = 2.00000
n = -2
```

Output:

```text
0.25000
```

Explanation:

```text
2^-2 = 1 / 2^2
     = 1 / 4
     = 0.25
```

## Approach

We use **Binary Exponentiation**, also called **Fast Power**.

A simple solution would multiply `x` by itself `n` times. However, this would take `O(n)` time.

Instead, we repeatedly square `x` and divide `n` by 2.

For example:

```text
2^10

2^10 = (2^5)^2
2^5  = 2 × 2^4
2^4  = (2^2)^2
2^2  = (2^1)^2
```

This allows us to calculate the result in `O(log n)` time.

## Handling Negative Powers

If `n` is negative, we use:

```text
x^(-n) = 1 / x^n
```

Therefore, when `n < 0`:

```python
x = 1 / x
n = -n
```

After this, we can calculate the power normally.

## Algorithm

1. If `n == 0`, return `1.0`.
2. If `n` is negative:
   - Change `x` to `1 / x`.
   - Make `n` positive.
3. Initialize `result = 1.0`.
4. While `n > 0`:
   - If `n` is odd, multiply `result` by `x`.
   - Square `x`.
   - Divide `n` by 2 using integer division.
5. Return `result`.

## Solution

```python
class Solution:
    def myPow(self, x, n):
        if n == 0:
            return 1.0

        if n < 0:
            x = 1 / x
            n = -n

        result = 1.0

        while n > 0:
            if n % 2 == 1:
                result *= x

            x *= x
            n //= 2

        return result
```

## Dry Run

For:

```text
x = 2
n = 10
```

Initially:

```text
result = 1
x = 2
n = 10
```

### Step 1

`n = 10` is even.

```text
x = 2 × 2 = 4
n = 10 // 2 = 5
```

### Step 2

`n = 5` is odd.

```text
result = 1 × 4 = 4
x = 4 × 4 = 16
n = 5 // 2 = 2
```

### Step 3

`n = 2` is even.

```text
x = 16 × 16 = 256
n = 2 // 2 = 1
```

### Step 4

`n = 1` is odd.

```text
result = 4 × 256 = 1024
n = 1 // 2 = 0
```

Now `n = 0`, so we return:

```text
1024
```

## Complexity

Let `n` be the exponent.

- **Time Complexity:** `O(log n)`
- **Space Complexity:** `O(1)`

The algorithm only uses a few variables and does not require additional data structures.

## Key Concept

The main idea is **Binary Exponentiation**:

```text
If n is even:
x^n = (x^(n/2))^2

If n is odd:
x^n = x × x^(n-1)
```

By repeatedly reducing the exponent by half, we achieve `O(log n)` time complexity.

## Constraints

- `-100.0 < x < 100.0`
- `-2^31 <= n <= 2^31 - 1`
- `n` is an integer.
- Either `x` is not zero or `n > 0`.
- `-10^4 <= x^n <= 10^4`

## Language

Python

## LeetCode Problem

Problem Number: **50**

Problem Name: **Pow(x, n)**

Difficulty: **Medium**
