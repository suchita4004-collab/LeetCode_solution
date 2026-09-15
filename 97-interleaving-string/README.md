```markdown
# 97. Interleaving String

**Difficulty:** Medium  
**Language:** Python

## Problem

Given three strings `s1`, `s2`, and `s3`, we have to check whether `s3` can be formed by interleaving `s1` and `s2`.

The characters of `s1` and `s2` must remain in their original order.

We can take characters from either string at each step.

For example:

```text
s1 = "ab"
s2 = "cd"
```

One possible interleaving is:

```text
a + c + b + d = "acbd"
```

So `"acbd"` is a valid interleaving.

---

## Important Condition

Before checking the interleaving, the lengths must satisfy:

```text
len(s1) + len(s2) = len(s3)
```

If this condition is not satisfied, `s3` cannot be formed.

---

## Examples

### Example 1

**Input:**

```text
s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
```

**Output:**

```text
true
```

One possible interleaving is:

```text
s1 = "aa" + "bc" + "c"
s2 = "dbbc" + "a"

"aa" + "dbbc" + "bc" + "a" + "c"

= "aadbbcbcac"
```

Therefore, the answer is `true`.

---

### Example 2

**Input:**

```text
s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbbaccc"
```

**Output:**

```text
false
```

It is not possible to form `s3` while maintaining the original order of characters in both strings.

---

### Example 3

**Input:**

```text
s1 = ""
s2 = ""
s3 = ""
```

**Output:**

```text
true
```

Two empty strings can form an empty string.

---

## Approach

I use **Dynamic Programming**.

At every position in `s3`, there are two possible choices:

1. Take the next character from `s1`.
2. Take the next character from `s2`.

We keep track of whether the characters processed so far can form the corresponding prefix of `s3`.

To save space, I use a **1D DP array**.

```text
dp[j]
```

represents whether:

```text
s1[:i] + s2[:j]
```

can form:

```text
s3[:i+j]
```

---

## Algorithm

1. Check whether:

```text
len(s1) + len(s2) == len(s3)
```

If not, return `False`.

2. Create a DP array of size `len(s2) + 1`.
3. Set `dp[0] = True`.
4. Fill the first row using only characters from `s2`.
5. Process each character of `s1`.
6. For every character of `s2`:
   - Check whether the current character can come from `s1`.
   - Check whether it can come from `s2`.
7. If either possibility is valid, set `dp[j] = True`.
8. Return the final DP value.

---

## Code

```python
class Solution:
    def isInterleave(self, s1, s2, s3):
        if len(s1) + len(s2) != len(s3):
            return False

        dp = [False] * (len(s2) + 1)
        dp[0] = True

        for j in range(1, len(s2) + 1):
            dp[j] = dp[j - 1] and s2[j - 1] == s3[j - 1]

        for i in range(1, len(s1) + 1):
            dp[0] = dp[0] and s1[i - 1] == s3[i - 1]

            for j in range(1, len(s2) + 1):
                from_s1 = (
                    dp[j] and
                    s1[i - 1] == s3[i + j - 1]
                )

                from_s2 = (
                    dp[j - 1] and
                    s2[j - 1] == s3[i + j - 1]
                )

                dp[j] = from_s1 or from_s2

        return dp[len(s2)]
```

---

## Dry Run

Consider:

```text
s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
```

Initially:

```text
dp[0] = True
```

We process characters from both strings.

At each position, we check whether the next character of `s3` matches:

```text
Next character from s1
        OR
Next character from s2
```

For example, at the beginning:

```text
s1 → a
s2 → d
s3 → a
```

The first character `a` matches the first character of `s1`.

So we can take:

```text
a from s1
```

Now:

```text
s1 → a
s2 → d
s3 → a a ...
```

The next `a` can again come from `s1`.

Later, characters can be taken from `s2`, while maintaining the order of both strings.

One valid sequence is:

```text
s1: aa + bc + c
s2: dbbc + a

Result:
aa + dbbc + bc + a + c

= aadbbcbcac
```

Therefore:

```text
Output = true
```

---

## How Code Works

### 1. Check Length

```python
if len(s1) + len(s2) != len(s3):
    return False
```

If the total number of characters is different, an interleaving is impossible.

---

### 2. Create DP Array

```python
dp = [False] * (len(s2) + 1)
```

The array stores whether a particular combination of prefixes is possible.

---

### 3. Base Case

```python
dp[0] = True
```

Two empty prefixes can form an empty string.

---

### 4. Take Character From `s1`

```python
from_s1 = (
    dp[j] and
    s1[i - 1] == s3[i + j - 1]
)
```

This checks whether the current character of `s1` can be used.

---

### 5. Take Character From `s2`

```python
from_s2 = (
    dp[j - 1] and
    s2[j - 1] == s3[i + j - 1]
)
```

This checks whether the current character of `s2` can be used.

---

### 6. Either Choice Works

```python
dp[j] = from_s1 or from_s2
```

If either string can provide the required character, the current state is possible.

---

## DP Idea

The basic idea can be represented as:

```text
                  s3 current character
                         |
              ┌──────────┴──────────┐
              ↓                     ↓
       Take from s1           Take from s2
              ↓                     ↓
        Check previous         Check previous
           state                  state
              └──────────┬──────────┘
                         ↓
                  Possible / Not
```

We don't change the order of characters inside either string.

---

## Important Edge Cases

### 1. All Strings Empty

```text
s1 = ""
s2 = ""
s3 = ""

Output = true
```

### 2. Lengths Don't Match

```text
s1 = "ab"
s2 = "cd"
s3 = "abc"
```

Since:

```text
2 + 2 != 3
```

the answer is immediately `false`.

### 3. One String Is Empty

For example:

```text
s1 = ""
s2 = "abc"
s3 = "abc"
```

Output:

```text
true
```

### 4. Same Characters but Wrong Order

The characters must maintain their original order.

For example, if the required order cannot be maintained, the result is `false`.

---

## Complexity Analysis

Let:

```text
m = len(s1)
n = len(s2)
```

We process every combination of positions from the two strings.

**Time Complexity:** `O(m × n)`

**Space Complexity:** `O(n)`

We use a 1D DP array instead of a full 2D table.

---

## Key Concept

The main concept used in this problem is **Dynamic Programming**.

At every step we have two choices:

```text
Take character from s1
          OR
Take character from s2
```

The important thing is that we never change the order of characters inside either string.

---

## Constraints

- `0 <= s1.length <= 100`
- `0 <= s2.length <= 100`
- `0 <= s3.length <= 200`
- `s1`, `s2`, and `s3` contain lowercase English letters.

---

## LeetCode Information

**Problem Number:** 97  
**Problem Name:** Interleaving String  
**Difficulty:** Medium  
**Topic:** Dynamic Programming, Strings

---

## File Structure

```text
97-interleaving-string/
│
├── README.md
└── solution.py
```

---

## Solution

[View solution.py](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/97-interleaving-string/solution.py)

---

## Repository

[LeetCode_solution](https://github.com/suchita4004-collab/LeetCode_solution)
```
