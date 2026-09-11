# Minimum Window Substring

## Problem

Given two strings `s` and `t`, find the **smallest substring of `s`** that contains every character of `t`.

The characters from `t` must be included **with their duplicates**.

If no such substring exists, return an empty string `""`.

### Example 1

**Input:**
```text
s = "ADOBECODEBANC"
t = "ABC"
```

**Output:**
```text
"BANC"
```

**Explanation:**

The substring `"BANC"` contains:

- `A`
- `B`
- `C`

It is the smallest valid window.

### Example 2

**Input:**
```text
s = "a"
t = "a"
```

**Output:**
```text
"a"
```

### Example 3

**Input:**
```text
s = "a"
t = "aa"
```

**Output:**
```text
""
```

**Explanation:**

`t` requires two `a` characters, but `s` contains only one `a`.

---

## Approach

We use the **Sliding Window** technique.

We maintain a window using two pointers:

```text
left
  ↓
[A D O B E C O D E B A N C]
                          ↑
                        right
```

The window expands using the `right` pointer.

When the window contains all required characters, we move `left` forward to make the window as small as possible.

Two dictionaries are used:

- `need` → stores the required frequency of every character in `t`
- `window` → stores the frequency of characters currently inside the window

We also maintain:

- `formed` → number of characters whose required frequency is completely satisfied
- `required` → total number of different characters required

---

## Algorithm

1. Create a frequency map `need` for string `t`.
2. Start `left = 0`.
3. Move `right` from left to right through string `s`.
4. Add `s[right]` to the current window.
5. If a character reaches its required frequency, increase `formed`.
6. When `formed == required`, the current window is valid.
7. Store the window if it is smaller than the previous answer.
8. Move `left` forward to shrink the window.
9. If removing a character makes the window invalid, decrease `formed`.
10. Continue until `right` reaches the end of `s`.
11. Return the smallest valid window.
12. If no valid window exists, return `""`.

---

## Dry Run

Consider:

```text
s = "ADOBECODEBANC"
t = "ABC"
```

Required characters:

```text
A → 1
B → 1
C → 1
```

As `right` moves:

```text
A D O B E C
```

The window now contains `A`, `B`, and `C`.

So it is a valid window:

```text
"ADOBEC"
```

Now we move `left` forward to reduce the size.

After removing unnecessary characters:

```text
"BEC"
```

is still not enough because it does not contain `A`.

Continue expanding the window.

Eventually we get:

```text
"BANC"
```

This contains:

```text
B → 1
A → 1
N → extra
C → 1
```

The minimum valid window is:

```text
"BANC"
```

Therefore:

```text
Output = "BANC"
```

---

## Handling Duplicate Characters

Duplicates in `t` are important.

For example:

```text
s = "a"
t = "aa"
```

The requirement is:

```text
a → 2
```

But the window contains only:

```text
a → 1
```

Therefore, the window is invalid and the answer is:

```text
""
```

Another example:

```text
t = "AABC"
```

requires:

```text
A → 2
B → 1
C → 1
```

The window must contain **two `A`s**, not just one.

---

## How the Code Works

### 1. Store required characters

```python
need = {}

for char in t:
    need[char] = need.get(char, 0) + 1
```

For:

```text
t = "AABC"
```

we get:

```text
{
    'A': 2,
    'B': 1,
    'C': 1
}
```

### 2. Expand the window

```python
for right in range(len(s)):
```

The `right` pointer moves forward and adds characters to the window.

### 3. Check whether a character is satisfied

```python
if char in need and window[char] == need[char]:
    formed += 1
```

When a required character reaches exactly its required frequency, `formed` is increased.

### 4. Shrink the window

```python
while formed == required:
```

This means the current window contains everything required by `t`.

We then move `left` forward to find a smaller valid window.

### 5. Save the minimum window

```python
if window_length < min_length:
    min_length = window_length
    min_left = left
```

Whenever we find a smaller valid window, we save its position.

### 6. Return the answer

```python
return s[min_left:min_left + min_length]
```

---

## Important Edge Cases

### Case 1: `t` is longer than `s`

```text
s = "a"
t = "aa"
```

Return:

```text
""
```

### Case 2: Exact match

```text
s = "abc"
t = "abc"
```

Return:

```text
"abc"
```

### Case 3: No possible window

```text
s = "abcdef"
t = "xyz"
```

Return:

```text
""
```

### Case 4: Duplicate characters

```text
s = "AAABC"
t = "AABC"
```

The answer must contain at least:

```text
A → 2
B → 1
C → 1
```

### Case 5: Extra characters

Extra characters are allowed in the window as long as all required characters are present.

---

## Complexity Analysis

Let:

- `m` = length of `s`
- `n` = length of `t`

### Time Complexity

```text
O(m + n)
```

We process the characters of `t` once and the characters of `s` using the sliding window.

Even though there is a nested `while` loop, both `left` and `right` only move forward.

### Space Complexity

```text
O(n)
```

The frequency maps store characters required from `t` and characters present in the window.

Since the problem contains only uppercase and lowercase English letters, the practical space usage is bounded by the character set.

---

## Key Concept

The main concept used is:

**Sliding Window**

The basic idea is:

```text
Expand → Make window valid → Shrink → Save minimum
```

Flow:

```text
        Expand right
             ↓
      Add character
             ↓
    Is window valid?
        /          \
      No            Yes
      ↓              ↓
 Continue       Shrink left
                       ↓
                Save minimum
                       ↓
                 Continue
```

---

## Constraints

- `1 <= m, n <= 10^5`
- `s` and `t` contain uppercase and lowercase English letters.
- The answer is unique for the given test cases.

---

## Language

**Python**

---

## LeetCode Information

- **Problem:** Minimum Window Substring
- **Problem Number:** 76
- **Difficulty:** Hard
- **Topic:** Sliding Window, Hash Map, Two Pointers

---

## File Structure

```text
LeetCode_solution/
│
├── 76-minimum-window-substring/
│   ├── solution.py
│   └── README.md
│
└── README.md
```

---

## Solution Link

[View Solution](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/76-minimum-window-substring/solution.py)

## Repository Link

[LeetCode_solution](https://github.com/suchita4004-collab/LeetCode_solution)# Minimum Window Substring

## Problem

Given two strings `s` and `t`, find the **smallest substring of `s`** that contains every character of `t`.

The characters from `t` must be included **with their duplicates**.

If no such substring exists, return an empty string `""`.

### Example 1

**Input:**
```text
s = "ADOBECODEBANC"
t = "ABC"
```

**Output:**
```text
"BANC"
```

**Explanation:**

The substring `"BANC"` contains:

- `A`
- `B`
- `C`

It is the smallest valid window.

### Example 2

**Input:**
```text
s = "a"
t = "a"
```

**Output:**
```text
"a"
```

### Example 3

**Input:**
```text
s = "a"
t = "aa"
```

**Output:**
```text
""
```

**Explanation:**

`t` requires two `a` characters, but `s` contains only one `a`.

---

## Approach

We use the **Sliding Window** technique.

We maintain a window using two pointers:

```text
left
  ↓
[A D O B E C O D E B A N C]
                          ↑
                        right
```

The window expands using the `right` pointer.

When the window contains all required characters, we move `left` forward to make the window as small as possible.

Two dictionaries are used:

- `need` → stores the required frequency of every character in `t`
- `window` → stores the frequency of characters currently inside the window

We also maintain:

- `formed` → number of characters whose required frequency is completely satisfied
- `required` → total number of different characters required

---

## Algorithm

1. Create a frequency map `need` for string `t`.
2. Start `left = 0`.
3. Move `right` from left to right through string `s`.
4. Add `s[right]` to the current window.
5. If a character reaches its required frequency, increase `formed`.
6. When `formed == required`, the current window is valid.
7. Store the window if it is smaller than the previous answer.
8. Move `left` forward to shrink the window.
9. If removing a character makes the window invalid, decrease `formed`.
10. Continue until `right` reaches the end of `s`.
11. Return the smallest valid window.
12. If no valid window exists, return `""`.

---

## Dry Run

Consider:

```text
s = "ADOBECODEBANC"
t = "ABC"
```

Required characters:

```text
A → 1
B → 1
C → 1
```

As `right` moves:

```text
A D O B E C
```

The window now contains `A`, `B`, and `C`.

So it is a valid window:

```text
"ADOBEC"
```

Now we move `left` forward to reduce the size.

After removing unnecessary characters:

```text
"BEC"
```

is still not enough because it does not contain `A`.

Continue expanding the window.

Eventually we get:

```text
"BANC"
```

This contains:

```text
B → 1
A → 1
N → extra
C → 1
```

The minimum valid window is:

```text
"BANC"
```

Therefore:

```text
Output = "BANC"
```

---

## Handling Duplicate Characters

Duplicates in `t` are important.

For example:

```text
s = "a"
t = "aa"
```

The requirement is:

```text
a → 2
```

But the window contains only:

```text
a → 1
```

Therefore, the window is invalid and the answer is:

```text
""
```

Another example:

```text
t = "AABC"
```

requires:

```text
A → 2
B → 1
C → 1
```

The window must contain **two `A`s**, not just one.

---

## How the Code Works

### 1. Store required characters

```python
need = {}

for char in t:
    need[char] = need.get(char, 0) + 1
```

For:

```text
t = "AABC"
```

we get:

```text
{
    'A': 2,
    'B': 1,
    'C': 1
}
```

### 2. Expand the window

```python
for right in range(len(s)):
```

The `right` pointer moves forward and adds characters to the window.

### 3. Check whether a character is satisfied

```python
if char in need and window[char] == need[char]:
    formed += 1
```

When a required character reaches exactly its required frequency, `formed` is increased.

### 4. Shrink the window

```python
while formed == required:
```

This means the current window contains everything required by `t`.

We then move `left` forward to find a smaller valid window.

### 5. Save the minimum window

```python
if window_length < min_length:
    min_length = window_length
    min_left = left
```

Whenever we find a smaller valid window, we save its position.

### 6. Return the answer

```python
return s[min_left:min_left + min_length]
```

---

## Important Edge Cases

### Case 1: `t` is longer than `s`

```text
s = "a"
t = "aa"
```

Return:

```text
""
```

### Case 2: Exact match

```text
s = "abc"
t = "abc"
```

Return:

```text
"abc"
```

### Case 3: No possible window

```text
s = "abcdef"
t = "xyz"
```

Return:

```text
""
```

### Case 4: Duplicate characters

```text
s = "AAABC"
t = "AABC"
```

The answer must contain at least:

```text
A → 2
B → 1
C → 1
```

### Case 5: Extra characters

Extra characters are allowed in the window as long as all required characters are present.

---

## Complexity Analysis

Let:

- `m` = length of `s`
- `n` = length of `t`

### Time Complexity

```text
O(m + n)
```

We process the characters of `t` once and the characters of `s` using the sliding window.

Even though there is a nested `while` loop, both `left` and `right` only move forward.

### Space Complexity

```text
O(n)
```

The frequency maps store characters required from `t` and characters present in the window.

Since the problem contains only uppercase and lowercase English letters, the practical space usage is bounded by the character set.

---

## Key Concept

The main concept used is:

**Sliding Window**

The basic idea is:

```text
Expand → Make window valid → Shrink → Save minimum
```

Flow:

```text
        Expand right
             ↓
      Add character
             ↓
    Is window valid?
        /          \
      No            Yes
      ↓              ↓
 Continue       Shrink left
                       ↓
                Save minimum
                       ↓
                 Continue
```

---

## Constraints

- `1 <= m, n <= 10^5`
- `s` and `t` contain uppercase and lowercase English letters.
- The answer is unique for the given test cases.

---

## Language

**Python**

---

## LeetCode Information

- **Problem:** Minimum Window Substring
- **Problem Number:** 76
- **Difficulty:** Hard
- **Topic:** Sliding Window, Hash Map, Two Pointers

---

## File Structure

```text
LeetCode_solution/
│
├── 76-minimum-window-substring/
│   ├── solution.py
│   └── README.md
│
└── README.md
```

---

## Solution Link

[View Solution](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/76-minimum-window-substring/solution.py)

## Repository Link

[LeetCode_solution](https://github.com/suchita4004-collab/LeetCode_solution)# Minimum Window Substring

## Problem

Given two strings `s` and `t`, find the **smallest substring of `s`** that contains every character of `t`.

The characters from `t` must be included **with their duplicates**.

If no such substring exists, return an empty string `""`.

### Example 1

**Input:**
```text
s = "ADOBECODEBANC"
t = "ABC"
```

**Output:**
```text
"BANC"
```

**Explanation:**

The substring `"BANC"` contains:

- `A`
- `B`
- `C`

It is the smallest valid window.

### Example 2

**Input:**
```text
s = "a"
t = "a"
```

**Output:**
```text
"a"
```

### Example 3

**Input:**
```text
s = "a"
t = "aa"
```

**Output:**
```text
""
```

**Explanation:**

`t` requires two `a` characters, but `s` contains only one `a`.

---

## Approach

We use the **Sliding Window** technique.

We maintain a window using two pointers:

```text
left
  ↓
[A D O B E C O D E B A N C]
                          ↑
                        right
```

The window expands using the `right` pointer.

When the window contains all required characters, we move `left` forward to make the window as small as possible.

Two dictionaries are used:

- `need` → stores the required frequency of every character in `t`
- `window` → stores the frequency of characters currently inside the window

We also maintain:

- `formed` → number of characters whose required frequency is completely satisfied
- `required` → total number of different characters required

---

## Algorithm

1. Create a frequency map `need` for string `t`.
2. Start `left = 0`.
3. Move `right` from left to right through string `s`.
4. Add `s[right]` to the current window.
5. If a character reaches its required frequency, increase `formed`.
6. When `formed == required`, the current window is valid.
7. Store the window if it is smaller than the previous answer.
8. Move `left` forward to shrink the window.
9. If removing a character makes the window invalid, decrease `formed`.
10. Continue until `right` reaches the end of `s`.
11. Return the smallest valid window.
12. If no valid window exists, return `""`.

---

## Dry Run

Consider:

```text
s = "ADOBECODEBANC"
t = "ABC"
```

Required characters:

```text
A → 1
B → 1
C → 1
```

As `right` moves:

```text
A D O B E C
```

The window now contains `A`, `B`, and `C`.

So it is a valid window:

```text
"ADOBEC"
```

Now we move `left` forward to reduce the size.

After removing unnecessary characters:

```text
"BEC"
```

is still not enough because it does not contain `A`.

Continue expanding the window.

Eventually we get:

```text
"BANC"
```

This contains:

```text
B → 1
A → 1
N → extra
C → 1
```

The minimum valid window is:

```text
"BANC"
```

Therefore:

```text
Output = "BANC"
```

---

## Handling Duplicate Characters

Duplicates in `t` are important.

For example:

```text
s = "a"
t = "aa"
```

The requirement is:

```text
a → 2
```

But the window contains only:

```text
a → 1
```

Therefore, the window is invalid and the answer is:

```text
""
```

Another example:

```text
t = "AABC"
```

requires:

```text
A → 2
B → 1
C → 1
```

The window must contain **two `A`s**, not just one.

---

## How the Code Works

### 1. Store required characters

```python
need = {}

for char in t:
    need[char] = need.get(char, 0) + 1
```

For:

```text
t = "AABC"
```

we get:

```text
{
    'A': 2,
    'B': 1,
    'C': 1
}
```

### 2. Expand the window

```python
for right in range(len(s)):
```

The `right` pointer moves forward and adds characters to the window.

### 3. Check whether a character is satisfied

```python
if char in need and window[char] == need[char]:
    formed += 1
```

When a required character reaches exactly its required frequency, `formed` is increased.

### 4. Shrink the window

```python
while formed == required:
```

This means the current window contains everything required by `t`.

We then move `left` forward to find a smaller valid window.

### 5. Save the minimum window

```python
if window_length < min_length:
    min_length = window_length
    min_left = left
```

Whenever we find a smaller valid window, we save its position.

### 6. Return the answer

```python
return s[min_left:min_left + min_length]
```

---

## Important Edge Cases

### Case 1: `t` is longer than `s`

```text
s = "a"
t = "aa"
```

Return:

```text
""
```

### Case 2: Exact match

```text
s = "abc"
t = "abc"
```

Return:

```text
"abc"
```

### Case 3: No possible window

```text
s = "abcdef"
t = "xyz"
```

Return:

```text
""
```

### Case 4: Duplicate characters

```text
s = "AAABC"
t = "AABC"
```

The answer must contain at least:

```text
A → 2
B → 1
C → 1
```

### Case 5: Extra characters

Extra characters are allowed in the window as long as all required characters are present.

---

## Complexity Analysis

Let:

- `m` = length of `s`
- `n` = length of `t`

### Time Complexity

```text
O(m + n)
```

We process the characters of `t` once and the characters of `s` using the sliding window.

Even though there is a nested `while` loop, both `left` and `right` only move forward.

### Space Complexity

```text
O(n)
```

The frequency maps store characters required from `t` and characters present in the window.

Since the problem contains only uppercase and lowercase English letters, the practical space usage is bounded by the character set.

---

## Key Concept

The main concept used is:

**Sliding Window**

The basic idea is:

```text
Expand → Make window valid → Shrink → Save minimum
```

Flow:

```text
        Expand right
             ↓
      Add character
             ↓
    Is window valid?
        /          \
      No            Yes
      ↓              ↓
 Continue       Shrink left
                       ↓
                Save minimum
                       ↓
                 Continue
```

---

## Constraints

- `1 <= m, n <= 10^5`
- `s` and `t` contain uppercase and lowercase English letters.
- The answer is unique for the given test cases.

---

## Language

**Python**

---

## LeetCode Information

- **Problem:** Minimum Window Substring
- **Problem Number:** 76
- **Difficulty:** Hard
- **Topic:** Sliding Window, Hash Map, Two Pointers

---

## File Structure

```text
LeetCode_solution/
│
├── 76-minimum-window-substring/
│   ├── solution.py
│   └── README.md
│
└── README.md
```

---

## Solution Link

[View Solution](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/76-minimum-window-substring/solution.py)

## Repository Link

[LeetCode_solution](https://github.com/suchita4004-collab/LeetCode_solution)
