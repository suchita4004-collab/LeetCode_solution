```markdown
# 91. Decode Ways

**Difficulty:** Medium  
**Language:** Python

## Problem

You are given a string `s` containing digits.

The digits can be decoded using the following mapping:

```text
1  → A
2  → B
3  → C
...
25 → Y
26 → Z
```

A number can be decoded in two ways:

- One digit at a time, such as `1 → A`
- Two digits together, such as `12 → L`

The task is to find the **total number of possible ways** to decode the complete string.

If the string cannot be decoded, return `0`.

---

## Examples

### Example 1

```text
Input:
s = "12"

Output:
2
```

Possible decodings:

```text
1 2  → AB
12   → L
```

Therefore, the answer is `2`.

---

### Example 2

```text
Input:
s = "226"

Output:
3
```

Possible decodings:

```text
2 2 6  → BBF
22 6   → VF
2 26   → BZ
```

Therefore:

```text
Output = 3
```

---

### Example 3

```text
Input:
s = "06"

Output:
0
```

`06` is invalid because a number cannot start with `0`.

Therefore:

```text
Output = 0
```

---

## Approach

We use **Dynamic Programming**.

At every position, we check two possibilities:

1. Can the current digit be decoded as a single digit?
2. Can the current and previous digits be decoded together as a two-digit number from `10` to `26`?

We keep track of the number of ways to decode the previous two positions.

Instead of using a complete DP array, we use only three variables:

```text
prev2
prev1
current
```

This reduces the space required.

---

## Important Rules

### Single Digit

A single digit is valid if it is from:

```text
1 to 9
```

So:

```text
1 → A
5 → E
9 → I
```

But:

```text
0
```

is not valid by itself.

---

### Two Digits

Two digits are valid if their value is between:

```text
10 and 26
```

For example:

```text
10 → J
12 → L
20 → T
26 → Z
```

But:

```text
27
30
06
```

are invalid two-digit codes.

---

## Algorithm

1. If the string is empty or starts with `0`, return `0`.
2. Initialize:
   ```text
   prev2 = 1
   prev1 = 1
   ```
3. Traverse the string from the second character.
4. Set `current = 0`.
5. If the current digit is not `0`, add `prev1` to `current`.
6. Check the previous and current digits as a two-digit number.
7. If the number is between `10` and `26`, add `prev2` to `current`.
8. Move the previous values forward.
9. Continue until the end of the string.
10. Return `prev1`.

---

## Code

```python
class Solution:
    def numDecodings(self, s):
        if not s or s[0] == '0':
            return 0

        prev2 = 1
        prev1 = 1

        for i in range(1, len(s)):
            current = 0

            # Decode one digit
            if s[i] != '0':
                current += prev1

            # Decode two digits
            two_digit = int(s[i - 1:i + 1])

            if 10 <= two_digit <= 26:
                current += prev2

            prev2 = prev1
            prev1 = current

        return prev1
```

---

## Dry Run

Consider:

```text
s = "226"
```

### Initial Values

```text
prev2 = 1
prev1 = 1
```

We process the string from left to right.

### First Character

The first character is:

```text
2
```

It is valid, so we have one way:

```text
2 → B
```

---

### Processing Second Character

Current digit:

```text
2
```

Single digit:

```text
2 → B
```

This gives the previous number of ways.

Two digits:

```text
22 → V
```

This is also valid.

Therefore:

```text
current = 2
```

Update:

```text
prev2 = 1
prev1 = 2
```

---

### Processing Third Character

Current digit:

```text
6
```

Single digit:

```text
6 → F
```

There are `2` ways before this digit, so:

```text
current += 2
```

Now check two digits:

```text
26 → Z
```

`26` is valid.

So:

```text
current += 1
```

Therefore:

```text
current = 3
```

Final answer:

```text
3
```

---

## Visual Representation

For:

```text
226
```

The possible groupings are:

```text
2 | 2 | 6
    ↓
   BBF

22 | 6
    ↓
   VF

2 | 26
    ↓
   BZ
```

Therefore:

```text
Total ways = 3
```

---

## How Code Works

### Checking a Single Digit

```python
if s[i] != '0':
    current += prev1
```

If the current digit is not zero, it can be decoded separately.

For example:

```text
6 → F
```

---

### Checking Two Digits

```python
two_digit = int(s[i - 1:i + 1])
```

This takes two consecutive digits.

For example:

```text
"26" → 26
```

Then:

```python
if 10 <= two_digit <= 26:
    current += prev2
```

Only values from `10` to `26` are valid two-digit codes.

---

## Handling Zero

Zero is important in this problem.

### Valid

```text
10 → J
20 → T
```

A zero can be used when it is part of `10` or `20`.

### Invalid

```text
06
30
00
```

These cannot be decoded.

For example:

```text
06
```

cannot be treated as:

```text
0 | 6
```

because `0` has no mapping.

---

## Why Dynamic Programming?

The same smaller decoding problems occur repeatedly.

For example, while decoding:

```text
226
```

we need the number of ways to decode earlier parts of the string.

Dynamic Programming stores these results instead of calculating them again.

The basic idea is:

```text
ways up to previous position
             ↓
      calculate current
             ↓
       ways up to current
```

---

## Important Edge Cases

### 1. String starts with zero

```text
Input:
"06"

Output:
0
```

---

### 2. Single valid digit

```text
Input:
"7"

Output:
1
```

Because:

```text
7 → G
```

---

### 3. Single zero

```text
Input:
"0"

Output:
0
```

There is no mapping for `0`.

---

### 4. Zero after a valid number

```text
Input:
"10"

Output:
1
```

Only:

```text
10 → J
```

is valid.

---

### 5. Invalid number greater than 26

```text
Input:
"27"

Output:
1
```

`27` cannot be used as a two-digit code, but:

```text
2 | 7 → BG
```

is valid.

---

### 6. Multiple zeros

```text
Input:
"100"

Output:
0
```

`10` is valid, but the remaining `0` cannot be decoded.

---

## Complexity Analysis

Let `n` be the length of the string.

### Time Complexity

```text
O(n)
```

We process each character once.

### Space Complexity

```text
O(1)
```

Only three variables are used, regardless of the size of the input.

---

## Key Concept

The main idea is:

> **At every position, check whether we can decode one digit or two digits, and add the number of ways from the previous positions.**

Remember:

```text
1–9   → valid single digit
10–26 → valid two digits
0     → cannot be decoded alone
```

---

## Constraints

- `1 <= s.length <= 100`
- `s` contains only digits.
- `s` may contain leading zeros.
- The answer fits in a 32-bit integer.

---

## LeetCode Information

- **Problem:** 91. Decode Ways
- **Difficulty:** Medium
- **Language:** Python
- **Topics:** String, Dynamic Programming

---

## File Structure

```text
91-decode-ways/
│
├── README.md
└── solution.py
```

---

## Solution

[View solution.py](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/91-decode-ways/solution.py)

## Repository

[LeetCode Solution Repository](https://github.com/suchita4004-collab/LeetCode_solution)
```
