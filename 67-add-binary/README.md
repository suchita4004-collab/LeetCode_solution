# 67 - Add Binary

## Problem

Given two binary strings `a` and `b`, return their **sum as a binary string**.

A binary number contains only:

```text
0 and 1
```

For example:

```text
11₂ + 1₂ = 100₂
```

The task is to add the two binary strings without converting the complete strings into decimal integers.

---

## Examples

### Example 1

**Input:**
```text
a = "11"
b = "1"
```

**Output:**
```text
"100"
```

**Explanation:**

```text
  11
+  1
----
 100
```

Therefore:

```text
11₂ + 1₂ = 100₂
```

---

### Example 2

**Input:**
```text
a = "1010"
b = "1011"
```

**Output:**
```text
"10101"
```

**Explanation:**

```text
  1010
+ 1011
------
 10101
```

Therefore:

```text
1010₂ + 1011₂ = 10101₂
```

---

## Approach

We perform binary addition exactly like normal decimal addition.

We start from the **rightmost digit** of both strings.

For every position:

```text
digit_a + digit_b + carry
```

The resulting binary digit is:

```text
total % 2
```

The carry is:

```text
total // 2
```

We continue until both strings and the carry are completely processed.

---

## Binary Addition Rules

The basic binary addition rules are:

| A | B | Carry In | Result | Carry Out |
|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 |
| 0 | 1 | 0 | 1 | 0 |
| 1 | 0 | 0 | 1 | 0 |
| 1 | 1 | 0 | 0 | 1 |
| 1 | 1 | 1 | 1 | 1 |

For example:

```text
1 + 1 = 10
```

So we write `0` and carry `1`.

---

## Algorithm

1. Set pointers `i` and `j` to the last positions of `a` and `b`.
2. Initialize `carry = 0`.
3. Create an empty result list.
4. While either string still has digits or there is a carry:
   - Get the current digit from `a`.
   - Get the current digit from `b`.
   - If one string has ended, use `0`.
   - Add both digits and the carry.
   - Store `total % 2` in the result.
   - Update carry using `total // 2`.
5. Reverse the result.
6. Join the digits into a string.
7. Return the binary string.

---

## Dry Run

Consider:

```text
a = "11"
b = "1"
```

Start from the right.

### Step 1

```text
1 + 1 + 0 = 2
```

Binary result:

```text
0
```

Carry:

```text
1
```

### Step 2

```text
1 + 0 + 1 = 2
```

Result:

```text
0
```

Carry:

```text
1
```

### Step 3

Both strings are finished, but carry is still `1`.

So:

```text
1
```

Result before reversing:

```text
[0, 0, 1]
```

After reversing:

```text
[1, 0, 0]
```

Final answer:

```text
"100"
```

---

## Solution

```python
class Solution:
    def addBinary(self, a, b):
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        result = []

        while i >= 0 or j >= 0 or carry:
            digit_a = int(a[i]) if i >= 0 else 0
            digit_b = int(b[j]) if j >= 0 else 0

            total = digit_a + digit_b + carry

            result.append(str(total % 2))
            carry = total // 2

            i -= 1
            j -= 1

        result.reverse()

        return "".join(result)
```

---

## How the Code Works

### 1. Start from the last digits

```python
i = len(a) - 1
j = len(b) - 1
```

We start from the right because binary addition works from the least significant digit.

---

### 2. Initialize carry

```python
carry = 0
```

Initially there is no carry.

---

### 3. Add the digits

```python
total = digit_a + digit_b + carry
```

We add:

- Current digit of `a`
- Current digit of `b`
- Previous carry

---

### 4. Calculate the result digit

```python
result.append(str(total % 2))
```

`total % 2` gives the current binary digit.

For example:

```text
2 % 2 = 0
3 % 2 = 1
```

---

### 5. Calculate carry

```python
carry = total // 2
```

For example:

```text
2 // 2 = 1
3 // 2 = 1
1 // 2 = 0
```

---

### 6. Move to the next digits

```python
i -= 1
j -= 1
```

We move from right to left.

---

### 7. Reverse the result

Because digits are added from right to left, the result is initially stored backwards.

```python
result.reverse()
```

Then:

```python
return "".join(result)
```

converts the list into a string.

---

## Important Edge Cases

### Both strings contain one digit

```text
"0" + "0" = "0"
```

### Different lengths

```text
"11" + "1" = "100"
```

### Carry continues through multiple digits

```text
"111" + "1" = "1000"
```

### Large strings

The strings can contain up to `10,000` digits, so processing them digit-by-digit is efficient.

---

## Complexity Analysis

Let `n` be the length of the larger string.

### Time Complexity

```text
O(n)
```

Each digit is processed once.

### Space Complexity

```text
O(n)
```

The result requires space proportional to the length of the output.

---

## Key Concept

The main concept used in this problem is:

**Binary Addition + Carry Handling**

The important formula is:

```text
result digit = total % 2
carry = total // 2
```

---

## Constraints

- `1 <= a.length, b.length <= 10⁴`
- `a` and `b` contain only `'0'` and `'1'`
- Neither string contains leading zeros except `"0"`

---

## Language

**Python**

---

## LeetCode Information

- **Problem Number:** 67
- **Problem Name:** Add Binary
- **Difficulty:** Easy
- **Topic:** Math, String, Bit Manipulation
- **Technique:** Binary Addition

---

## File Structure

```text
67-add-binary/
├── README.md
└── solution.py
```

---

## Solution Link

[View Solution](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/67-add-binary/solution.py)

---

## Repository Link

[LeetCode_solution](https://github.com/suchita4004-collab/LeetCode_solution)
