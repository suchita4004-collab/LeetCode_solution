```markdown
# 70 - Climbing Stairs

## Problem

You are climbing a staircase with `n` steps.

At each move, you can climb either:

- `1` step
- `2` steps

Find the total number of **distinct ways** to reach the top of the staircase.

---

## Examples

### Example 1

**Input:**
```text
n = 2
```

**Output:**
```text
2
```

**Explanation:**

There are two ways to reach the top:

1. `1 step + 1 step`
2. `2 steps`

---

### Example 2

**Input:**
```text
n = 3
```

**Output:**
```text
3
```

**Explanation:**

There are three ways to reach the top:

1. `1 step + 1 step + 1 step`
2. `1 step + 2 steps`
3. `2 steps + 1 step`

---

## Approach

This problem follows the **Fibonacci pattern**.

To reach step `n`, we can come from:

- Step `n - 1` by taking `1` step
- Step `n - 2` by taking `2` steps

Therefore:

```text
ways(n) = ways(n - 1) + ways(n - 2)
```

The first two values are:

```text
ways(1) = 1
ways(2) = 2
```

So the sequence becomes:

```text
1, 2, 3, 5, 8, 13, ...
```

---

## Algorithm

1. If `n` is `1` or `2`, return `n`.
2. Store the number of ways for the previous two steps.
3. Calculate the current number of ways using:
   ```text
   current = first + second
   ```
4. Move the values forward.
5. Return the final value.

---

## Dry Run

For:

```text
n = 5
```

Initial values:

```text
ways(1) = 1
ways(2) = 2
```

Calculate step by step:

```text
ways(3) = 1 + 2 = 3
ways(4) = 2 + 3 = 5
ways(5) = 3 + 5 = 8
```

Therefore:

```text
Output = 8
```

The 8 ways are:

```text
1 + 1 + 1 + 1 + 1
1 + 1 + 1 + 2
1 + 1 + 2 + 1
1 + 2 + 1 + 1
2 + 1 + 1 + 1
1 + 2 + 2
2 + 1 + 2
2 + 2 + 1
```

---

## Solution

```python
class Solution:
    def climbStairs(self, n):
        if n <= 2:
            return n

        first = 1
        second = 2

        for _ in range(3, n + 1):
            third = first + second
            first = second
            second = third

        return second
```

---

## How the Code Works

### 1. Handle small values

```python
if n <= 2:
    return n
```

For:

```text
n = 1 → 1 way
n = 2 → 2 ways
```

---

### 2. Store previous values

```python
first = 1
second = 2
```

These represent:

```text
first  → ways to reach step n-2
second → ways to reach step n-1
```

---

### 3. Calculate the next value

```python
third = first + second
```

The current number of ways is the sum of the previous two values.

---

### 4. Move the values forward

```python
first = second
second = third
```

This prepares the variables for the next iteration.

---

### 5. Return the answer

```python
return second
```

After the loop, `second` contains the total number of ways to reach the top.

---

## Important Edge Cases

### Case 1: `n = 1`

```text
Output = 1
```

Only:

```text
1
```

---

### Case 2: `n = 2`

```text
Output = 2
```

Ways:

```text
1 + 1
2
```

---

### Case 3: `n = 3`

```text
Output = 3
```

Ways:

```text
1 + 1 + 1
1 + 2
2 + 1
```

---

## Complexity Analysis

### Time Complexity

```text
O(n)
```

We calculate the answer for each step from `3` to `n`.

### Space Complexity

```text
O(1)
```

Only three variables are used, so no extra array is required.

---

## Key Concept

The main concept used in this problem is **Dynamic Programming**.

It also follows the **Fibonacci sequence**:

```text
1, 2, 3, 5, 8, 13, ...
```

The important formula is:

```text
ways(n) = ways(n - 1) + ways(n - 2)
```

---

## Constraints

```text
1 <= n <= 45
```

---

## Language

**Python**

---

## LeetCode Information

- **Problem:** Climbing Stairs
- **Problem Number:** 70
- **Difficulty:** Easy
- **Topic:** Dynamic Programming
- **Pattern:** Fibonacci

---

## File Structure

```text
70-climbing-stairs/
├── README.md
└── solution.py
```

---

## Solution Link

[View Solution](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/70-climbing-stairs/solution.py)

---

## Repository Link

[LeetCode_solution](https://github.com/suchita4004-collab/LeetCode_solution)
```
