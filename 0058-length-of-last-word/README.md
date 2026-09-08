# 0058 - Length of Last Word

## Problem

Given a string `s` consisting of words and spaces, return the length of the **last word** in the string.

A word is a maximal substring consisting of non-space characters only.

The string may contain spaces at the beginning or end, and there may be multiple spaces between words.

## Examples

### Example 1

Input:

```text
s = "Hello World"
```

Output:

```text
5
```

Explanation:

The last word is `"World"`, which has a length of `5`.

### Example 2

Input:

```text
s = "   fly me   to   the moon  "
```

Output:

```text
4
```

Explanation:

The last word is `"moon"`, which has a length of `4`.

### Example 3

Input:

```text
s = "luffy is still joyboy"
```

Output:

```text
6
```

Explanation:

The last word is `"joyboy"`, which has a length of `6`.

## Approach

We can solve this problem efficiently by scanning the string from **right to left**.

There may be spaces after the last word, so first we skip all trailing spaces.

Once we reach the last word, we count its characters until we reach another space or the beginning of the string.

## Algorithm

1. Start from the last character of the string.
2. Skip all trailing spaces.
3. Initialize `count = 0`.
4. Continue moving from right to left.
5. For every non-space character, increase `count`.
6. Stop when a space is found or the beginning of the string is reached.
7. Return `count`.

## Solution

```python
class Solution:
    def lengthOfLastWord(self, s):
        i = len(s) - 1

        # Skip trailing spaces
        while i >= 0 and s[i] == ' ':
            i -= 1

        count = 0

        # Count characters of the last word
        while i >= 0 and s[i] != ' ':
            count += 1
            i -= 1

        return count
```

## Dry Run

Consider:

```text
s = "Hello World"
```

Start from the end:

```text
H e l l o   W o r l d
                  ↑
```

The last character is `d`.

We count:

```text
d → 1
l → 2
r → 3
o → 4
W → 5
```

The next character is a space, so we stop.

Therefore:

```text
Answer = 5
```

## Dry Run with Trailing Spaces

Consider:

```text
s = "Hello World   "
```

First, skip the trailing spaces:

```text
"Hello World   "
           ↑
```

After skipping spaces, we reach `d`.

Now count the characters:

```text
d → 1
l → 2
r → 3
o → 4
W → 5
```

The next character is a space.

Therefore:

```text
Answer = 5
```

## Complexity

Let `n` be the length of the string.

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`

We scan the string from right to left and use only a few variables.

## Key Concept

The main idea is:

```text
Start from the end
       ↓
Skip spaces
       ↓
Count last word
       ↓
Stop at space
```

This approach avoids creating additional strings or using extra data structures.

## Alternative Approach

Python also provides the `split()` method:

```python
class Solution:
    def lengthOfLastWord(self, s):
        return len(s.split()[-1])
```

However, this creates a list of words and therefore uses additional memory.

The main solution above uses **constant extra space**, making it more memory efficient.

## Constraints

- `1 <= s.length <= 10^4`
- `s` consists of English letters and spaces `' '`.
- There is at least one word in `s`.

## Language

Python

## LeetCode Problem

**Problem Number:** 58

**Problem Name:** Length of Last Word

**Difficulty:** Easy

## Solution Link

[View Solution on GitHub](solution.py)

## Problem Link

[LeetCode – Length of Last Word](https://leetcode.com/problems/length-of-last-word/)
