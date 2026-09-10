# 69 - Sqrt(x)

## Problem

Given a non-negative integer `x`, return the **square root of `x` rounded down** to the nearest integer.

The returned value must also be non-negative.

You must **not use any built-in exponent function or operator**.

For example, the following are not allowed:

```text
pow(x, 0.5)
x ** 0.5
```

The answer should be the largest integer `n` such that:

```text
n × n <= x
```

---

## Examples

### Example 1

**Input:**

```text
x = 4
```

**Output:**

```text
2
```

**Explanation:**

```text
√4 = 2
```

Therefore, the answer is:

```text
2
```

---

### Example 2

**Input:**

```text
x = 8
```

**Output:**

```text
2
```

**Explanation:**

```text
√8 = 2.82842...
```

After rounding down:

```text
2
```

---

## Approach

We use **Binary Search**.

Instead of checking every number from `1` to `x`, we search for the square root efficiently.

For a number `mid`:

```text
mid × mid <= x
```

If this is true, `mid` can be a possible answer.

If:

```text
mid × mid > x
```

then `mid` is too large, so we search on the left side.

---

## Why Binary Search?

Suppose:

```text
x = 8
```

We need to find:

```text
2 × 2 <= 8
3 × 3 > 8
```

Therefore:

```text
sqrt(8) = 2
```

Binary search reduces the number of comparisons significantly.

---

## Algorithm

1. If `x` is `0` or `1`, return `x`.
2. Set:
   - `left = 1`
   - `right = x // 2`
3. Find the middle value:
   ```text
   mid = (left + right) // 2
   ```
4. Check whether `mid × mid <= x`.
5. If true:
   - Store `mid` as the current answer.
   - Search for a larger possible answer.
6. Otherwise:
   - Search on the left side.
7. Return the largest valid value.

---

## Dry Run

Consider:

```text
x = 8
```

Initial:

```text
left = 1
right = 4
answer = 0
```

### Step 1

```text
mid = (1 + 4) // 2
    = 2
```

Check:

```text
2 × 2 = 4 <= 8
```

So `2` is valid.

```text
answer = 2
left = 3
```

### Step 2

```text
mid = (3 + 4) // 2
    = 3
```

Check:

```text
3 × 3 = 9 > 8
```

So `3` is too large.

```text
right = 2
```

Now:

```text
left = 3
right = 2
```

The search ends.

Return:

```text
2
```

---

## Important Overflow Handling

Instead of directly checking:

```python
mid * mid <= x
```

we use:

```python
mid <= x // mid
```

This avoids unnecessary multiplication and is safer for large integer values.

For example:

```text
mid <= x // mid
```

means:

```text
mid × mid <= x
```

---

## Solution

```python
class Solution:
    def mySqrt(self, x):
        if x < 2:
            return x

        left = 1
        right = x // 2
        answer = 0

        while left <= right:
            mid = (left + right) // 2

            if mid <= x // mid:
                answer = mid
                left = mid + 1
            else:
                right = mid - 1

        return answer
```

---

## How the Code Works

### 1. Handle 0 and 1

```python
if x < 2:
    return x
```

The square roots are:

```text
√0 = 0
√1 = 1
```

So we can directly return `x`.

---

### 2. Set the search range

```python
left = 1
right = x // 2
```

For every `x >= 2`, its integer square root cannot be greater than `x // 2`.

---

### 3. Find the middle

```python
mid = (left + right) // 2
```

This divides the search range into two parts.

---

### 4. Check the square

```python
if mid <= x // mid:
```

This checks whether:

```text
mid × mid <= x
```

If it is valid, we store it:

```python
answer = mid
```

Then we try to find a larger valid value:

```python
left = mid + 1
```

---

### 5. If mid is too large

```python
else:
    right = mid - 1
```

We move to the left half because all larger numbers will also be too large.

---

### 6. Return the answer

```python
return answer
```

The largest valid integer is returned.

---

## Important Edge Cases

### x = 0

```text
0 → 0
```

### x = 1

```text
1 → 1
```

### Perfect square

```text
4 → 2
9 → 3
16 → 4
```

### Non-perfect square

```text
8 → 2
10 → 3
15 → 3
```

The result is always rounded down.

---

## Complexity Analysis

### Time Complexity

```text
O(log x)
```

Binary search reduces the search space by approximately half in every iteration.

### Space Complexity

```text
O(1)
```

Only a few variables are used.

---

## Key Concept

The main concept used in this problem is:

**Binary Search**

We search for the largest integer satisfying:

```text
n × n <= x
```

---

## Constraints

- `0 <= x <= 2³¹ - 1`

---

## Language

**Python**

---

## LeetCode Information

- **Problem Number:** 69
- **Problem Name:** Sqrt(x)
- **Difficulty:** Easy
- **Topic:** Math, Binary Search
- **Technique:** Binary Search

---

## File Structure

```text
69-sqrtx/
├── README.md
└── solution.py
```

---

## Solution Link

[View Solution](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/69-sqrtx/solution.py)

---

## Repository Link

[LeetCode_solution](https://github.com/suchita4004-collab/LeetCode_solution)
