# 66 - Plus One

## Problem

You are given a **large integer** represented as an array of digits.

Each element `digits[i]` represents one digit of the integer.

The digits are arranged from the **most significant digit to the least significant digit**.

The task is to **increment the integer by one** and return the resulting array of digits.

For example:

```text
[1,2,3]
```

represents:

```text
123
```

After adding one:

```text
123 + 1 = 124
```

Therefore, the answer is:

```text
[1,2,4]
```

---

## Examples

### Example 1

**Input:**
```text
digits = [1,2,3]
```

**Output:**
```text
[1,2,4]
```

**Explanation:**

The array represents `123`.

```text
123 + 1 = 124
```

So the result is:

```text
[1,2,4]
```

---

### Example 2

**Input:**
```text
digits = [4,3,2,1]
```

**Output:**
```text
[4,3,2,2]
```

**Explanation:**

The array represents `4321`.

```text
4321 + 1 = 4322
```

So the result is:

```text
[4,3,2,2]
```

---

### Example 3

**Input:**
```text
digits = [9]
```

**Output:**
```text
[1,0]
```

**Explanation:**

The array represents `9`.

```text
9 + 1 = 10
```

So the result is:

```text
[1,0]
```

---

## Approach

We start from the **last digit** because adding one affects the number from the right side.

There are two main cases:

### Case 1: Last digit is less than 9

For example:

```text
[1,2,3]
```

The last digit is `3`.

Add one:

```text
3 + 1 = 4
```

Result:

```text
[1,2,4]
```

We can immediately return the result.

---

### Case 2: Last digit is 9

For example:

```text
[1,2,9]
```

Adding one to `9` creates a carry:

```text
9 + 1 = 10
```

So we change `9` to `0` and carry `1` to the previous digit.

```text
[1,2,9]
      ↓
[1,3,0]
```

If the previous digit is also `9`, the carry continues.

---

## Algorithm

1. Start from the last digit.
2. Move from right to left.
3. If the current digit is less than `9`:
   - Add `1`.
   - Return the array.
4. If the current digit is `9`:
   - Change it to `0`.
   - Continue to the previous digit.
5. If every digit was `9`, add `1` at the beginning.
6. Return the resulting array.

---

## Dry Run

Consider:

```text
digits = [1,2,9]
```

### Step 1

Start from the last digit:

```text
9
```

Since it is `9`, change it to `0`.

```text
[1,2,0]
```

Carry `1` to the previous digit.

### Step 2

Previous digit:

```text
2
```

Since `2 < 9`, add `1`.

```text
[1,3,0]
```

Return:

```text
[1,3,0]
```

---

## Dry Run for All 9s

Consider:

```text
digits = [9,9,9]
```

### Step 1

```text
[9,9,9]
      ↓
[9,9,0]
```

### Step 2

```text
[9,9,0]
    ↓
[9,0,0]
```

### Step 3

```text
[9,0,0]
  ↓
[0,0,0]
```

All digits were `9`, so add `1` at the beginning:

```text
[1,0,0,0]
```

Therefore:

```text
999 + 1 = 1000
```

---

## Solution

```python
class Solution:
    def plusOne(self, digits):
        # Start from the last digit
        for i in range(len(digits) - 1, -1, -1):

            # If digit is less than 9, simply add 1
            if digits[i] < 9:
                digits[i] += 1
                return digits

            # If digit is 9, make it 0 and carry 1
            digits[i] = 0

        # If all digits were 9, add 1 at the beginning
        return [1] + digits
```

---

## How the Code Works

### 1. Start from the last digit

```python
for i in range(len(digits) - 1, -1, -1):
```

We traverse the array from **right to left**.

This is necessary because addition starts from the least significant digit.

---

### 2. Check if digit is less than 9

```python
if digits[i] < 9:
    digits[i] += 1
    return digits
```

If the digit is not `9`, we can simply increase it by one.

Example:

```text
[1,2,3]
```

becomes:

```text
[1,2,4]
```

---

### 3. Handle digit 9

```python
digits[i] = 0
```

When the digit is `9`:

```text
9 + 1 = 10
```

So the current digit becomes `0` and the carry moves to the left.

---

### 4. Handle all 9s

```python
return [1] + digits
```

If the loop finishes, it means every digit was `9`.

For example:

```text
[9,9,9]
```

becomes:

```text
[1,0,0,0]
```

---

## Important Edge Cases

### Normal number

```text
[1,2,3] → [1,2,4]
```

### Last digit is 9

```text
[1,2,9] → [1,3,0]
```

### Multiple 9s

```text
[1,9,9] → [2,0,0]
```

### All digits are 9

```text
[9,9,9] → [1,0,0,0]
```

### Single digit

```text
[5] → [6]
```

---

## Complexity Analysis

### Time Complexity

```text
O(n)
```

In the worst case, all digits are `9`, so we may traverse the complete array.

### Space Complexity

```text
O(1)
```

Apart from the result `[1] + digits` in the all-9 case, no additional data structure is required.

---

## Key Concept

The main concept used in this problem is:

**Array Traversal + Carry Handling**

The important idea is:

```text
Start from right → Add 1 → Handle carry → Move left
```

---

## Constraints

- `1 <= digits.length <= 100`
- `0 <= digits[i] <= 9`
- `digits` does not contain any leading `0`s.

---

## Language

**Python**

---

## LeetCode Information

- **Problem Number:** 66
- **Problem Name:** Plus One
- **Difficulty:** Easy
- **Topic:** Array
- **Technique:** Carry Handling

---

## File Structure

```text
66-plus-one/
├── README.md
└── solution.py
```

---

## Solution Link

[View Solution](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/66-plus-one/solution.py)

---

## Repository Link

[LeetCode_solution](https://github.com/suchita4004-collab/LeetCode_solution)
