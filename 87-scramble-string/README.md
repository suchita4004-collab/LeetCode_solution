# 87. Scramble String

**Difficulty:** Hard  
**Language:** Python

## Problem

Given two strings `s1` and `s2` of the same length, determine whether `s2` is a scrambled version of `s1`.

A string can be scrambled by:

1. Splitting it into two non-empty parts.
2. Swapping the two parts or keeping them in the same order.
3. Repeating the same process recursively on the resulting parts.

### Example

```text
Input:  s1 = "great", s2 = "rgeat"
Output: true
```

Explanation:

```text
great
 /   \
gr    eat

Swap "gr" → "rg"

rg + eat = rgeat
```

So `"rgeat"` is a scrambled version of `"great"`.

---

## Examples

### Example 1

```text
Input:
s1 = "great"
s2 = "rgeat"

Output:
true
```

### Example 2

```text
Input:
s1 = "abcde"
s2 = "caebd"

Output:
false
```

### Example 3

```text
Input:
s1 = "a"
s2 = "a"

Output:
true
```

---

## Approach

This problem can be solved using **Recursion + Memoization**.

We try every possible position to split `s1` into two parts.

For every split, there are two possibilities:

### 1. No Swap

The left part of `s1` matches the left part of `s2`, and the right part matches the right part.

```text
s1 = A | B
s2 = C | D

A matches C
B matches D
```

### 2. Swap

The left part of `s1` matches the right part of `s2`, and the right part matches the left part.

```text
s1 = A | B
s2 = D | C

A matches C
B matches D
```

If any split works, the strings are scrambled versions of each other.

---

## Important Character Check

Before trying all possible splits, we check whether both strings contain the same characters.

For example:

```text
s1 = "great"
s2 = "rgeat"
```

Both contain the same characters:

```text
a, e, g, r, t
```

Therefore, they can possibly be scrambled versions.

But:

```text
s1 = "abcde"
s2 = "caebd"
```

do not have the same character frequencies, so we can immediately return `False`.

This check helps reduce unnecessary recursion.

---

## Algorithm

1. Create a dictionary called `memo` to store already calculated results.
2. Define a recursive function `solve(a, b)`.
3. If `a` and `b` are exactly the same, return `True`.
4. If their lengths are different, return `False`.
5. Check whether the result for `(a, b)` is already stored in `memo`.
6. Check whether both strings contain the same characters.
7. Try every possible split position.
8. Check the **no-swap case**.
9. Check the **swap case**.
10. If any case is successful, store `True` in `memo`.
11. If no split works, store `False`.
12. Return the final result.

---

## Code

```python
class Solution:
    def isScramble(self, s1, s2):
        memo = {}

        def solve(a, b):
            # Same strings are always scrambled versions
            if a == b:
                return True

            # Different lengths cannot be scrambled
            if len(a) != len(b):
                return False

            key = (a, b)

            # Return already calculated result
            if key in memo:
                return memo[key]

            # Scrambled strings must contain the same characters
            if sorted(a) != sorted(b):
                memo[key] = False
                return False

            n = len(a)

            # Try every possible split
            for i in range(1, n):

                # Case 1: No swap
                if solve(a[:i], b[:i]) and solve(a[i:], b[i:]):
                    memo[key] = True
                    return True

                # Case 2: Swap
                if solve(a[:i], b[n-i:]) and solve(a[i:], b[:n-i]):
                    memo[key] = True
                    return True

            memo[key] = False
            return False

        return solve(s1, s2)
```

---

## Dry Run

Consider:

```text
s1 = "great"
s2 = "rgeat"
```

We can split `s1` as:

```text
gr | eat
```

For `s2`:

```text
rg | eat
```

The first parts are:

```text
gr
rg
```

They do not match directly.

So we try the **swap case**.

```text
gr → rg
eat → eat
```

Both parts can be scrambled successfully.

Therefore:

```text
Output = True
```

---

## How Code Works

The main function calls:

```python
solve(s1, s2)
```

The recursive function tries different split positions.

For example:

```text
great
```

can be split as:

```text
g | reat
gr | eat
gre | at
grea | t
```

For each split, the program checks both possible arrangements.

### No-Swap Case

```python
solve(a[:i], b[:i]) and solve(a[i:], b[i:])
```

This checks:

```text
A | B
C | D

A → C
B → D
```

### Swap Case

```python
solve(a[:i], b[n-i:]) and solve(a[i:], b[:n-i])
```

This checks:

```text
A | B
D | C

A → C
B → D
```

If either case is successful, the current strings are scrambled versions.

---

## Why Memoization Is Important

Without memoization, the same substring combinations may be checked many times.

For example:

```text
solve("great", "rgeat")
```

can create many smaller recursive calls.

The dictionary:

```python
memo = {}
```

stores the result for each pair:

```text
(a, b)
```

So if the same pair appears again, we directly return its stored result.

This avoids repeated calculations.

---

## Recursion Structure

The recursive process can be represented as:

```text
              solve(s1, s2)
                     |
              Try every split
                     |
          -----------------------
          |                     |
       No Swap                Swap
          |                     |
       A → C                  A → D
       B → D                  B → C
          |                     |
          ---------+-------------
                   |
             Any successful?
              /          \
            Yes           No
             |             |
          True           False
```

---

## Important Edge Cases

### 1. Both strings are equal

```text
s1 = "abc"
s2 = "abc"
```

Output:

```text
true
```

### 2. Different lengths

```text
s1 = "abc"
s2 = "abcd"
```

Output:

```text
false
```

### 3. Different characters

```text
s1 = "abc"
s2 = "abd"
```

Output:

```text
false
```

### 4. Single character

```text
s1 = "a"
s2 = "a"
```

Output:

```text
true
```

---

## Complexity Analysis

Let `n` be the length of the strings.

The recursive solution with memoization has a high worst-case complexity because it considers many substring pairs and split positions.

```text
Time Complexity: O(n^4) approximately
Space Complexity: O(n^3)
```

The exact practical performance is improved by memoization and the character-frequency check.

---

## Key Concept

The main idea is:

> **Try every possible split and check both swapped and non-swapped arrangements recursively.**

Memoization prevents the same subproblem from being solved repeatedly.

---

## Difference Between Scrambling and Rearranging

A scramble is not simply any random rearrangement of characters.

The rearrangement must be produced by repeatedly:

```text
Split → Swap or Don't Swap → Split Again
```

For example:

```text
great
```

can become:

```text
rgeat
```

through valid recursive splitting and swapping.

---

## Constraints

- `1 <= s1.length, s2.length <= 30`
- `s1.length == s2.length`
- `s1` and `s2` consist of lowercase English letters.

---

## LeetCode Information

- **Problem:** 87. Scramble String
- **Difficulty:** Hard
- **Language:** Python
- **Topic:** Recursion, Dynamic Programming, Memoization, Strings

---

## File Structure

```text
87-scramble-string/
│
├── README.md
└── solution.py
```

---

## Solution

[View solution.py](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/87-scramble-string/solution.py)

## Repository

[LeetCode Solution Repository](https://github.com/suchita4004-collab/LeetCode_solution)
