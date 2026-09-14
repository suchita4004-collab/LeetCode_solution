```markdown
# 93. Restore IP Addresses

**Difficulty:** Medium  
**Language:** Python

## Problem

Given a string `s` containing only digits, we have to insert exactly three dots to create a valid IP address.

A valid IP address has exactly four parts.

Each part must:

- Be between `0` and `255`.
- Not contain leading zeros.
- Contain at most 3 digits.
- Use all the digits from the given string without changing their order.

We need to return all possible valid IP addresses.

---

## Examples

### Example 1

**Input:**
```text
s = "25525511135"
```

**Output:**
```text
["255.255.11.135", "255.255.111.35"]
```

### Example 2

**Input:**
```text
s = "0000"
```

**Output:**
```text
["0.0.0.0"]
```

### Example 3

**Input:**
```text
s = "101023"
```

**Output:**
```text
["1.0.10.23",
 "1.0.102.3",
 "10.1.0.23",
 "10.10.2.3",
 "101.0.2.3"]
```

---

## Approach

I use **Backtracking** to try different ways of dividing the string into four parts.

For every part, I try taking:

- 1 digit
- 2 digits
- 3 digits

Before adding a part, I check:

1. It should not have a leading zero.
2. Its value should not be greater than `255`.
3. Finally, there must be exactly four parts using all digits.

If all four parts are valid, I join them using dots and add the IP address to the result.

---

## Algorithm

1. Create an empty result list.
2. Start from the first digit.
3. Choose 1, 2, or 3 digits for the current IP part.
4. Check whether the selected part is valid.
5. Add the part and recursively process the remaining digits.
6. After returning from recursion, remove the last part using backtracking.
7. When four parts are formed:
   - If all digits are used, add the IP address to the result.
8. Return the result.

---

## Code

```python
class Solution:
    def restoreIpAddresses(self, s):
        result = []

        def backtrack(start, parts):
            if len(parts) == 4:
                if start == len(s):
                    result.append(".".join(parts))
                return

            remaining = len(s) - start
            needed = 4 - len(parts)

            if remaining < needed or remaining > needed * 3:
                return

            for length in range(1, 4):
                if start + length > len(s):
                    break

                part = s[start:start + length]

                if len(part) > 1 and part[0] == '0':
                    continue

                if int(part) > 255:
                    continue

                parts.append(part)
                backtrack(start + length, parts)
                parts.pop()

        backtrack(0, [])

        return result
```

---

## Dry Run

For:

```text
s = "25525511135"
```

The backtracking tries different divisions.

One valid division is:

```text
255 | 255 | 11 | 135
```

So:

```text
255.255.11.135
```

Another valid division is:

```text
255 | 255 | 111 | 35
```

So:

```text
255.255.111.35
```

Both are added to the result.

Final output:

```text
["255.255.11.135", "255.255.111.35"]
```

---

## How Code Works

### 1. Start Backtracking

```python
backtrack(0, [])
```

We start from index `0` with no IP parts.

### 2. Select 1 to 3 digits

```python
for length in range(1, 4):
```

An IP part can have a maximum of 3 digits.

### 3. Check Leading Zero

```python
if len(part) > 1 and part[0] == '0':
    continue
```

For example:

```text
01
001
```

are invalid.

But:

```text
0
```

is valid.

### 4. Check Range

```python
if int(part) > 255:
    continue
```

For example:

```text
255 → valid
256 → invalid
999 → invalid
```

### 5. Add the Part

```python
parts.append(part)
```

Then we recursively select the next part.

### 6. Backtrack

```python
parts.pop()
```

This removes the last selected part so that another possibility can be tried.

### 7. Create Final IP

When four valid parts are formed:

```python
result.append(".".join(parts))
```

For example:

```text
["192", "168", "1", "1"]
```

becomes:

```text
192.168.1.1
```

---

## Important Edge Cases

### Case 1: All zeros

```text
Input: "0000"
Output: ["0.0.0.0"]
```

We cannot create:

```text
00.0.0.0
0.00.0.0
```

because leading zeros are not allowed.

### Case 2: Number greater than 255

```text
256
```

cannot be an IP part.

### Case 3: Too few digits

An IP address needs at least 4 digits.

For example:

```text
"123"
```

cannot form a valid IP address.

### Case 4: Too many digits

Each of the four parts can have at most 3 digits, so more than 12 digits cannot form a valid IP address.

### Case 5: Leading zeros

```text
"01"
```

is invalid, while:

```text
"0"
```

is valid.

---

## Complexity Analysis

There are at most 3 choices for each of the 4 IP parts.

Therefore, the number of possible combinations is small.

**Time Complexity:** `O(3^4)` for generating possible partitions, plus the cost of building the result strings.

Since there are only four parts, this is effectively constant with respect to the input size for valid IP construction.

**Space Complexity:** `O(4)` for the recursion and current IP parts, excluding the output list.

---

## Key Concept

The main concept used in this problem is:

**Backtracking**

Backtracking means:

1. Choose an option.
2. Check whether it is valid.
3. Continue with the choice.
4. Undo the choice.
5. Try another option.

Here, we use it to try different ways of placing three dots in the string.

---

## Constraints

- `1 <= s.length <= 20`
- `s` consists only of digits.
- Each IP address must contain exactly four parts.
- Each part must be between `0` and `255`.
- Leading zeros are not allowed.

---

## LeetCode Information

**Problem Number:** 93  
**Problem Name:** Restore IP Addresses  
**Difficulty:** Medium  
**Topic:** Backtracking, String

---

## File Structure

```text
93-restore-ip-addresses/
│
├── README.md
└── solution.py
```

---

## Solution

[View solution.py](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/93-restore-ip-addresses/solution.py)

---

## Repository

[LeetCode_solution](https://github.com/suchita4004-collab/LeetCode_solution)
```
