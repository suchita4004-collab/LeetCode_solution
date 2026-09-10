# 65 - Valid Number

## Problem

Given a string `s`, determine whether it represents a **valid number**.

A valid number can be:

- An integer
- A decimal number
- An integer or decimal followed by an exponent

A number may contain an optional `+` or `-` sign.

Examples of valid numbers:

```text
"2"
"0089"
"-0.1"
"+3.14"
"4."
"-.9"
"2e10"
"-90E3"
"3e+7"
"+6e-1"
"53.5e93"
"-123.456e789"
```

Examples of invalid numbers:

```text
"abc"
"1a"
"1e"
"e3"
"99e2.5"
"--6"
"-+3"
"95a54e53"
```

---

## Examples

### Example 1

**Input:**
```text
s = "0"
```

**Output:**
```text
true
```

**Explanation:**

`"0"` contains a valid integer number.

---

### Example 2

**Input:**
```text
s = "e"
```

**Output:**
```text
false
```

**Explanation:**

An exponent cannot appear without a number before it.

---

### Example 3

**Input:**
```text
s = "."
```

**Output:**
```text
false
```

**Explanation:**

A decimal point must have at least one digit before or after it.

---

## Approach

We scan the string from **left to right** and check each part of the number.

The number can contain four important parts:

1. Optional sign `+` or `-`
2. Digits
3. Optional decimal point `.`
4. Optional exponent `e` or `E` followed by an integer

For example:

```text
-123.45e+6
│ │     │
│ │     └── Exponent
│ └──────── Decimal number
└────────── Sign
```

We make sure that every part follows the rules of a valid number.

---

## Algorithm

1. Start from index `0`.
2. Check whether the first character is `+` or `-`.
3. Read all digits before the decimal point.
4. If a `.` exists:
   - Skip the decimal point.
   - Read all digits after it.
5. Make sure there is at least one digit before or after the decimal point.
6. Check whether `e` or `E` exists.
7. If an exponent exists:
   - Check for an optional `+` or `-`.
   - Read the exponent digits.
   - Make sure at least one exponent digit exists.
8. Finally, check that the complete string has been processed.
9. Return `True` if all rules are satisfied; otherwise return `False`.

---

## Dry Run

Consider:

```text
s = "-123.45e+6"
```

### Step 1: Sign

```text
-
```

Valid optional sign.

### Step 2: Digits before decimal

```text
123
```

Valid digits.

### Step 3: Decimal point

```text
.
```

Valid decimal point.

### Step 4: Digits after decimal

```text
45
```

Valid digits.

### Step 5: Exponent

```text
e+6
```

- `e` → valid exponent
- `+` → valid exponent sign
- `6` → valid exponent digit

Therefore:

```text
True
```

---

## Important Cases

### Integer

```text
"2"       → True
"0089"    → True
"-123"    → True
"+5"      → True
```

### Decimal

```text
"3.14"    → True
"4."      → True
".9"      → True
"-.9"     → True
```

### Exponent

```text
"2e10"    → True
"3e+7"    → True
"6e-1"    → True
"-90E3"   → True
```

### Invalid Values

```text
"abc"     → False
"1a"      → False
"1e"      → False
"e3"      → False
"99e2.5"  → False
"--6"     → False
"-+3"     → False
"."       → False
```

---

## Solution

```python
class Solution:
    def isNumber(self, s):
        i = 0
        n = len(s)

        # Check optional sign
        if i < n and (s[i] == '+' or s[i] == '-'):
            i += 1

        digits_before = 0
        digits_after = 0

        # Check digits before decimal point
        while i < n and s[i].isdigit():
            digits_before += 1
            i += 1

        # Check decimal point and digits after it
        if i < n and s[i] == '.':
            i += 1

            while i < n and s[i].isdigit():
                digits_after += 1
                i += 1

        # At least one digit is required
        if digits_before == 0 and digits_after == 0:
            return False

        # Check exponent
        if i < n and (s[i] == 'e' or s[i] == 'E'):
            i += 1

            # Optional exponent sign
            if i < n and (s[i] == '+' or s[i] == '-'):
                i += 1

            exponent_digits = 0

            while i < n and s[i].isdigit():
                exponent_digits += 1
                i += 1

            # Exponent must contain at least one digit
            if exponent_digits == 0:
                return False

        return i == n
```

---

## How the Code Works

### 1. Check the sign

```python
if i < n and (s[i] == '+' or s[i] == '-'):
    i += 1
```

A number can optionally start with `+` or `-`.

---

### 2. Read digits before decimal

```python
while i < n and s[i].isdigit():
    digits_before += 1
    i += 1
```

This counts the digits before `.`.

---

### 3. Check decimal part

```python
if i < n and s[i] == '.':
```

A decimal point is allowed.

For example:

```text
4.
.9
3.14
```

All are valid because there is at least one digit somewhere in the number.

---

### 4. Check that a digit exists

```python
if digits_before == 0 and digits_after == 0:
    return False
```

This rejects:

```text
"."
"+."
"-."
```

---

### 5. Check exponent

```python
if i < n and (s[i] == 'e' or s[i] == 'E'):
```

An exponent can use either lowercase `e` or uppercase `E`.

For example:

```text
2e10
3E7
```

The exponent can also have a sign:

```text
3e+7
6e-1
```

---

### 6. Exponent must contain digits

```python
if exponent_digits == 0:
    return False
```

Therefore:

```text
"1e"    → False
"1e+"   → False
"1e-"   → False
```

---

### 7. Check the complete string

```python
return i == n
```

This makes sure there are no invalid characters remaining.

For example:

```text
"95a54e53"
```

contains `a`, so the entire string cannot be processed as a valid number.

---

## Important Edge Cases

| Input | Output |
|---|---|
| `"0"` | `True` |
| `"2"` | `True` |
| `"-0.1"` | `True` |
| `"4."` | `True` |
| `".9"` | `True` |
| `"2e10"` | `True` |
| `"3e+7"` | `True` |
| `"1e"` | `False` |
| `"e3"` | `False` |
| `"."` | `False` |
| `"99e2.5"` | `False` |
| `"--6"` | `False` |
| `"-+3"` | `False` |
| `"abc"` | `False` |

---

## Complexity Analysis

### Time Complexity

```text
O(n)
```

We scan the string at most once.

### Space Complexity

```text
O(1)
```

Only a few variables are used.

---

## Key Concept

The main concept used in this problem is:

**String Parsing**

We carefully validate:

```text
Sign → Digits → Decimal → Exponent
```

The important rule is that the entire string must follow the valid-number format.

---

## Constraints

- `1 <= s.length <= 20`
- `s` consists only of:
  - English letters
  - Digits `0-9`
  - `+`
  - `-`
  - `.`

---

## Language

**Python**

---

## LeetCode Information

- **Problem Number:** 65
- **Problem Name:** Valid Number
- **Difficulty:** Hard
- **Topic:** String
- **Technique:** String Parsing

---

## File Structure

```text
65-valid-number/
├── README.md
└── solution.py
```

---

## Solution Link

[View Solution](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/65-valid-number/solution.py)

---

## Repository Link

[LeetCode_solution](https://github.com/suchita4004-collab/LeetCode_solution)
