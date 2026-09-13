```markdown
# 89. Gray Code

**Difficulty:** Medium  
**Language:** Python

## Problem

An **n-bit Gray code sequence** contains `2^n` integers.

The sequence must satisfy the following conditions:

- It starts with `0`.
- Every number appears only once.
- Every number is between `0` and `2^n - 1`.
- Two adjacent numbers differ by exactly **one bit** in their binary representation.
- The first and last numbers must also differ by exactly one bit.

Given an integer `n`, return any valid Gray code sequence.

---

## Examples

### Example 1

```text
Input:
n = 2

Output:
[0,1,3,2]
```

Binary representation:

```text
0 → 00
1 → 01
3 → 11
2 → 10
```

Checking adjacent values:

```text
00 → 01   differ by 1 bit
01 → 11   differ by 1 bit
11 → 10   differ by 1 bit
10 → 00   differ by 1 bit
```

Therefore, `[0,1,3,2]` is a valid Gray code sequence.

Another valid answer is:

```text
[0,2,3,1]
```

### Example 2

```text
Input:
n = 1

Output:
[0,1]
```

Binary representation:

```text
0 → 0
1 → 1
```

They differ by exactly one bit.

---

## Approach

We use the **Reflection Method** to generate the Gray code.

We start with:

```text
[0]
```

For every bit position, we:

1. Take the current sequence.
2. Read it in reverse order.
3. Add `2^i` to every number in the reversed sequence.
4. Append these new values to the original sequence.

This creates a valid Gray code sequence.

---

## How Reflection Works

### For n = 1

Start with:

```text
[0]
```

Add `1` to the reversed sequence:

```text
[0] + [1]
```

Result:

```text
[0,1]
```

### For n = 2

Start with:

```text
[0,1]
```

Reverse it:

```text
[1,0]
```

Add `2`:

```text
[3,2]
```

Append:

```text
[0,1,3,2]
```

Binary:

```text
00
01
11
10
```

Each adjacent pair differs by one bit.

### For n = 3

Start with:

```text
[0,1,3,2]
```

Reverse:

```text
[2,3,1,0]
```

Add `4`:

```text
[6,7,5,4]
```

Append:

```text
[0,1,3,2,6,7,5,4]
```

Binary representation:

```text
000
001
011
010
110
111
101
100
```

Again, adjacent values differ by exactly one bit.

---

## Algorithm

1. Create a list `result` containing `0`.
2. Loop from `0` to `n - 1`.
3. Calculate `2^i` using:
   ```python
   1 << i
   ```
4. Traverse the current `result` list from right to left.
5. Add `2^i` to each value.
6. Append the new values to `result`.
7. Return `result`.

---

## Code

```python
class Solution:
    def grayCode(self, n):
        result = [0]

        for i in range(n):
            add = 1 << i

            for j in range(len(result) - 1, -1, -1):
                result.append(result[j] + add)

        return result
```

---

## Dry Run

Consider:

```text
n = 2
```

### Initial

```text
result = [0]
```

### First iteration

```text
i = 0

add = 1 << 0
add = 1
```

Current list:

```text
[0]
```

Reverse traversal:

```text
0
```

Add `1`:

```text
0 + 1 = 1
```

Result:

```text
[0,1]
```

### Second iteration

```text
i = 1

add = 1 << 1
add = 2
```

Current list:

```text
[0,1]
```

Read from right to left:

```text
1, 0
```

Add `2`:

```text
1 + 2 = 3
0 + 2 = 2
```

Append them:

```text
[0,1,3,2]
```

Final answer:

```text
[0,1,3,2]
```

---

## How Code Works

### Starting Value

```python
result = [0]
```

Every Gray code sequence starts with `0`.

### Calculate the New Bit

```python
add = 1 << i
```

This calculates:

```text
i = 0 → 1
i = 1 → 2
i = 2 → 4
i = 3 → 8
```

Each iteration introduces a new bit.

### Traverse in Reverse

```python
for j in range(len(result) - 1, -1, -1):
```

We traverse the existing sequence from the end to the beginning.

This is called the **reflection method**.

### Create New Values

```python
result.append(result[j] + add)
```

The new bit is added to each reflected value.

---

## Why Do We Traverse Backwards?

Suppose we have:

```text
[0,1]
```

If we reverse it:

```text
[1,0]
```

and add `2`:

```text
[3,2]
```

We get:

```text
[0,1,3,2]
```

The boundary is:

```text
01 → 11
```

Only one bit changes.

The last value is:

```text
10
```

and the first value is:

```text
00
```

Again, only one bit changes.

Therefore, reversing the sequence is important for maintaining the Gray code property.

---

## Visual Representation

For `n = 2`:

```text
       00
      /  \
     01  10
      \  /
       11
```

A valid traversal is:

```text
00 → 01 → 11 → 10 → 00
```

Each step changes exactly one bit.

---

## Important Edge Cases

### n = 1

```text
Input:
1

Output:
[0,1]
```

### n = 2

```text
Input:
2

Output:
[0,1,3,2]
```

### n = 0

The given constraints do not include `n = 0`, but the algorithm would return:

```text
[0]
```

---

## Complexity Analysis

For `n` bits, the sequence contains:

```text
2^n
```

elements.

### Time Complexity

```text
O(2^n)
```

Every generated value is processed once.

### Space Complexity

```text
O(2^n)
```

The result list contains `2^n` values.

---

## Key Concept

The main idea is:

> **Create the next Gray code by reflecting the current sequence and adding a new bit to the reflected values.**

For example:

```text
[0,1]
```

becomes:

```text
[0,1] + [3,2]
```

giving:

```text
[0,1,3,2]
```

---

## Constraints

- `1 <= n <= 16`
- The answer contains `2^n` integers.
- Every integer is in the range `[0, 2^n - 1]`.

---

## LeetCode Information

- **Problem:** 89. Gray Code
- **Difficulty:** Medium
- **Language:** Python
- **Topics:** Math, Backtracking, Bit Manipulation

---

## File Structure

```text
89-gray-code/
│
├── README.md
└── solution.py
```

---

## Solution

[View solution.py](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/89-gray-code/solution.py)

## Repository

[LeetCode Solution Repository](https://github.com/suchita4004-collab/LeetCode_solution)
```
