```markdown id="k7w2px"
# 72 - Edit Distance

## Problem

Given two strings `word1` and `word2`, find the **minimum number of operations** required to convert `word1` into `word2`.

We can perform three operations:

1. **Insert** a character
2. **Delete** a character
3. **Replace** a character

The goal is to use the minimum possible number of operations.

---

## Examples

### Example 1

**Input:**
```text
word1 = "horse"
word2 = "ros"
```

**Output:**
```text
3
```

**Explanation:**

```text
horse → rorse
```

Replace `h` with `r`.

```text
rorse → rose
```

Remove `r`.

```text
rose → ros
```

Remove `e`.

Total operations:

```text
3
```

---

### Example 2

**Input:**
```text
word1 = "intention"
word2 = "execution"
```

**Output:**
```text
5
```

**Explanation:**

One possible sequence is:

```text
intention → inention
```

Remove `t`.

```text
inention → enention
```

Replace `i` with `e`.

```text
enention → exention
```

Replace `n` with `x`.

```text
exention → exection
```

Replace `n` with `c`.

```text
exection → execution
```

Insert `u`.

Total operations:

```text
5
```

---

## Approach

This problem can be solved using **Dynamic Programming (DP)**.

We create a DP table where:

```text
dp[i][j]
```

represents the minimum number of operations required to convert:

```text
word1[0:i]
```

into:

```text
word2[0:j]
```

For every pair of characters, we have two cases.

### Case 1: Characters are the same

If:

```text
word1[i - 1] == word2[j - 1]
```

No operation is needed.

So:

```text
dp[i][j] = dp[i - 1][j - 1]
```

### Case 2: Characters are different

We can perform one of three operations:

- Insert
- Delete
- Replace

So we choose the operation requiring the minimum number of operations.

```text
dp[i][j] = 1 + min(insert, delete, replace)
```

---

## DP Formula

If the characters are equal:

```text
dp[i][j] = dp[i - 1][j - 1]
```

If the characters are different:

```text
dp[i][j] = 1 + min(
    dp[i][j - 1],       # Insert
    dp[i - 1][j],       # Delete
    dp[i - 1][j - 1]    # Replace
)
```

---

## Algorithm

1. Find the lengths of `word1` and `word2`.
2. Create a DP table of size `(m + 1) × (n + 1)`.
3. Initialize the first row.
4. Initialize the first column.
5. Compare each character of the two strings.
6. If characters are equal, copy the diagonal value.
7. If characters are different:
   - Calculate insert cost.
   - Calculate delete cost.
   - Calculate replace cost.
   - Take the minimum and add `1`.
8. Return `dp[m][n]`.

---

## Why Do We Initialize the First Row and Column?

Suppose `word1` is empty.

To convert an empty string into a string of length `j`, we need `j` insertions.

For example:

```text
"" → "abc"
```

requires:

```text
3 insertions
```

Therefore:

```text
dp[0][j] = j
```

Similarly, to convert a string of length `i` into an empty string, we need `i` deletions.

Therefore:

```text
dp[i][0] = i
```

---

## Dry Run

Consider:

```text
word1 = "horse"
word2 = "ros"
```

The DP table looks like:

```text
       ""  r  o  s
    ""  0  1  2  3
     h  1  1  2  3
     o  2  2  1  2
     r  3  2  2  2
     s  4  3  3  2
     e  5  4  4  3
```

The final value is:

```text
dp[5][3] = 3
```

Therefore:

```text
Minimum operations = 3
```

---

## Understanding the Three Operations

### 1. Insert

Insert a character into `word1`.

Example:

```text
"cat" → "cart"
```

Insert `r`.

---

### 2. Delete

Remove a character from `word1`.

Example:

```text
"cart" → "cat"
```

Delete `r`.

---

### 3. Replace

Replace one character with another.

Example:

```text
"cat" → "bat"
```

Replace `c` with `b`.

---

## Solution

```python id="4y9c8m"
class Solution:
    def minDistance(self, word1, word2):
        m = len(word1)
        n = len(word2)

        # dp[i][j] = minimum operations to convert
        # word1[:i] into word2[:j]
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Convert empty word1 to word2
        for j in range(n + 1):
            dp[0][j] = j

        # Convert word1 to an empty word2
        for i in range(m + 1):
            dp[i][0] = i

        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):

                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]

                else:
                    insert = dp[i][j - 1]
                    delete = dp[i - 1][j]
                    replace = dp[i - 1][j - 1]

                    dp[i][j] = 1 + min(insert, delete, replace)

        return dp[m][n]
```

---

## How the Code Works

### 1. Get string lengths

```python
m = len(word1)
n = len(word2)
```

`m` is the length of `word1` and `n` is the length of `word2`.

---

### 2. Create the DP table

```python
dp = [[0] * (n + 1) for _ in range(m + 1)]
```

The extra row and column represent the empty string.

---

### 3. Initialize the first row

```python
for j in range(n + 1):
    dp[0][j] = j
```

This represents converting an empty string into `word2`.

Only insertions are required.

---

### 4. Initialize the first column

```python
for i in range(m + 1):
    dp[i][0] = i
```

This represents converting `word1` into an empty string.

Only deletions are required.

---

### 5. Compare characters

```python
if word1[i - 1] == word2[j - 1]:
    dp[i][j] = dp[i - 1][j - 1]
```

If both characters are the same, no new operation is required.

---

### 6. Handle different characters

```python
insert = dp[i][j - 1]
delete = dp[i - 1][j]
replace = dp[i - 1][j - 1]
```

We calculate the cost of all three operations.

Then:

```python
dp[i][j] = 1 + min(insert, delete, replace)
```

We select the cheapest operation.

---

### 7. Return the answer

```python
return dp[m][n]
```

The bottom-right cell contains the minimum number of operations required.

---

## Important Edge Cases

### Case 1: Both strings are empty

```text
word1 = ""
word2 = ""
```

Output:

```text
0
```

No operation is required.

---

### Case 2: `word1` is empty

```text
word1 = ""
word2 = "abc"
```

Output:

```text
3
```

We need three insertions.

---

### Case 3: `word2` is empty

```text
word1 = "abc"
word2 = ""
```

Output:

```text
3
```

We need three deletions.

---

### Case 4: Both strings are equal

```text
word1 = "hello"
word2 = "hello"
```

Output:

```text
0
```

No changes are required.

---

## Complexity Analysis

Let:

```text
m = length of word1
n = length of word2
```

### Time Complexity

```text
O(m × n)
```

We fill every cell of the DP table once.

### Space Complexity

```text
O(m × n)
```

We store the complete DP table.

---

## Key Concept

The main concept used in this problem is:

**Dynamic Programming**

The three possible operations are:

```text
Insert
Delete
Replace
```

At every position, we choose the operation with the minimum cost.

The important formula is:

```text
dp[i][j] = 1 + min(
    insert,
    delete,
    replace
)
```

---

## Constraints

```text
0 <= word1.length, word2.length <= 500
```

`word1` and `word2` consist only of lowercase English letters.

---

## Language

**Python**

---

## LeetCode Information

- **Problem:** Edit Distance
- **Problem Number:** 72
- **Difficulty:** Medium
- **Topic:** Dynamic Programming
- **Pattern:** String DP

---

## File Structure

```text
72-edit-distance/
├── README.md
└── solution.py
```

---

## Solution Link

[View Solution](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/72-edit-distance/solution.py)

---

## Repository Link

[LeetCode_solution](https://github.com/suchita4004-collab/LeetCode_solution)
```
