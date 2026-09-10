# 68 - Text Justification

## Problem

Given an array of strings `words` and an integer `maxWidth`, format the text so that every line contains exactly `maxWidth` characters and is **fully justified**.

Words should be packed using a **greedy approach**, meaning we put as many words as possible on each line.

Extra spaces must be distributed as evenly as possible between the words.

If the spaces cannot be distributed equally, the gaps on the **left side receive more spaces**.

The **last line** must be left-justified.

---

## Rules

### 1. Greedy Packing

Put as many words as possible in each line without exceeding `maxWidth`.

### 2. Even Space Distribution

For a fully justified line:

```text
total spaces = maxWidth - total word length
```

These spaces are distributed between the gaps.

### 3. Extra Spaces

If spaces cannot be divided equally:

```text
Left gaps get extra spaces
```

### 4. Last Line

The last line is always **left-justified**.

Only one space is placed between words, and the remaining spaces are added at the end.

### 5. Single Word

A line containing only one word is also left-justified.

---

## Examples

### Example 1

**Input:**

```text
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
```

**Output:**

```text
[
    "This    is    an",
    "example  of text",
    "justification.  "
]
```

**Explanation:**

The first line contains:

```text
"This" + "is" + "an"
```

There are `8` spaces to distribute among `2` gaps.

So:

```text
4 spaces + 4 spaces
```

Result:

```text
"This    is    an"
```

---

### Example 2

**Input:**

```text
words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
```

**Output:**

```text
[
    "What   must   be",
    "acknowledgment  ",
    "shall be        "
]
```

**Explanation:**

The last line is:

```text
"shall be        "
```

It is left-justified because the last line does not use full justification.

The second line contains only one word, so it is also left-justified.

---

### Example 3

**Input:**

```text
words = [
    "Science","is","what","we","understand","well",
    "enough","to","explain","to","a","computer.",
    "Art","is","everything","else","we","do"
]

maxWidth = 20
```

**Output:**

```text
[
    "Science  is  what we",
    "understand          well",
    "enough to explain to",
    "a  computer.  Art is",
    "everything  else  we",
    "do                  "
]
```

---

## Approach

We use a **Greedy Algorithm**.

For every line:

1. Take as many words as possible.
2. Check whether the next word can fit.
3. Calculate the number of spaces needed.
4. If it is the last line or contains one word:
   - Put one space between words.
   - Add remaining spaces at the end.
5. Otherwise:
   - Distribute spaces equally between gaps.
   - Give extra spaces to the gaps on the left.

---

## Algorithm

1. Create an empty result list.
2. Start from the first word.
3. Keep adding words while they fit within `maxWidth`.
4. Calculate the total length of the words.
5. Check whether the line is the last line or contains only one word.
6. If yes:
   - Join words using one space.
   - Add spaces at the end.
7. Otherwise:
   - Calculate total spaces.
   - Calculate the number of gaps.
   - Calculate spaces per gap.
   - Calculate extra spaces.
   - Add extra spaces to the leftmost gaps.
8. Add the completed line to the result.
9. Continue until all words are processed.
10. Return the result.

---

## Dry Run

Consider:

```text
words = ["This", "is", "an", "example"]
maxWidth = 16
```

### Step 1: Pack words

First line:

```text
This is an
```

Word lengths:

```text
This = 4
is   = 2
an   = 2
```

Total word length:

```text
4 + 2 + 2 = 8
```

Maximum width:

```text
16
```

Therefore, required spaces:

```text
16 - 8 = 8
```

There are:

```text
3 - 1 = 2 gaps
```

Spaces per gap:

```text
8 // 2 = 4
```

Extra spaces:

```text
8 % 2 = 0
```

So the line becomes:

```text
"This    is    an"
```

Length:

```text
4 + 4 + 2 + 4 + 2 = 16
```

---

## Dry Run with Extra Spaces

Suppose:

```text
words = ["What", "must", "be"]
maxWidth = 16
```

Word length:

```text
4 + 4 + 2 = 10
```

Required spaces:

```text
16 - 10 = 6
```

Number of gaps:

```text
2
```

Spaces per gap:

```text
6 // 2 = 3
```

Extra spaces:

```text
6 % 2 = 0
```

Result:

```text
"What   must   be"
```

---

## Handling Unequal Spaces

Suppose there are `7` spaces and `3` gaps.

```text
7 // 3 = 2
7 % 3 = 1
```

Therefore:

```text
First gap  = 3 spaces
Second gap = 2 spaces
Third gap  = 2 spaces
```

The extra space goes to the **leftmost gap**.

---

## Solution

```python
class Solution:
    def fullJustify(self, words, maxWidth):
        result = []
        i = 0

        while i < len(words):
            line_words = []
            line_length = 0

            # Pack as many words as possible
            while i < len(words):
                word_length = len(words[i])

                if line_length + word_length + len(line_words) > maxWidth:
                    break

                line_words.append(words[i])
                line_length += word_length
                i += 1

            # Last line or line with only one word
            if i == len(words) or len(line_words) == 1:
                line = " ".join(line_words)
                line += " " * (maxWidth - len(line))
                result.append(line)
                continue

            # Fully justify the line
            total_spaces = maxWidth - line_length
            gaps = len(line_words) - 1

            spaces = total_spaces // gaps
            extra_spaces = total_spaces % gaps

            line = ""

            for j in range(gaps):
                line += line_words[j]
                line += " " * (spaces + (1 if j < extra_spaces else 0))

            line += line_words[-1]

            result.append(line)

        return result
```

---

## How the Code Works

### 1. Store the result

```python
result = []
```

This list stores all completed lines.

---

### 2. Pack words greedily

```python
while i < len(words):
```

We process the words one line at a time.

Inside this loop:

```python
if line_length + word_length + len(line_words) > maxWidth:
    break
```

The `len(line_words)` accounts for the minimum one space required between already selected words.

---

### 3. Handle the last line

```python
if i == len(words) or len(line_words) == 1:
```

The last line and a single-word line are left-justified.

For example:

```text
"shall be        "
```

---

### 4. Calculate spaces

```python
total_spaces = maxWidth - line_length
```

This gives the number of spaces that need to be distributed.

---

### 5. Calculate gaps

```python
gaps = len(line_words) - 1
```

For:

```text
"This is an"
```

there are two gaps:

```text
This | is | an
     ↑    ↑
```

---

### 6. Calculate spaces per gap

```python
spaces = total_spaces // gaps
```

This gives the minimum number of spaces each gap receives.

---

### 7. Calculate extra spaces

```python
extra_spaces = total_spaces % gaps
```

If spaces cannot be divided equally, these extra spaces are assigned from left to right.

---

### 8. Add extra spaces to the left

```python
line += " " * (spaces + (1 if j < extra_spaces else 0))
```

For example, if:

```text
spaces = 2
extra_spaces = 1
```

the gaps receive:

```text
3 spaces
2 spaces
2 spaces
```

---

## Important Edge Cases

### One word

```text
["Hello"]
```

Output:

```text
"Hello     "
```

---

### Last line

The last line is always left-justified.

```text
"shall be        "
```

---

### Word exactly equals maxWidth

```text
["Hello"]
maxWidth = 5
```

Output:

```text
"Hello"
```

---

### Unequal space distribution

Extra spaces always go to the leftmost gaps.

---

## Complexity Analysis

Let `N` be the total number of characters in all words.

### Time Complexity

```text
O(N)
```

Every word and every character is processed a limited number of times.

### Space Complexity

```text
O(N)
```

The output lines require space proportional to the final formatted text.

---

## Key Concept

The main concepts used in this problem are:

- **Greedy Algorithm**
- **String Manipulation**
- **Space Distribution**

The most important rule is:

```text
Extra spaces → Leftmost gaps
Last line → Left justified
Single word → Left justified
```

---

## Constraints

- `1 <= words.length <= 300`
- `1 <= words[i].length <= 20`
- `1 <= maxWidth <= 100`
- `words[i].length <= maxWidth`
- `words[i]` contains only English letters and symbols.

---

## Language

**Python**

---

## LeetCode Information

- **Problem Number:** 68
- **Problem Name:** Text Justification
- **Difficulty:** Hard
- **Topic:** Array, String
- **Technique:** Greedy

---

## File Structure

```text
68-text-justification/
├── README.md
└── solution.py
```

---

## Solution Link

[View Solution](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/68-text-justification/solution.py)

---

## Repository Link

[LeetCode_solution](https://github.com/suchita4004-collab/LeetCode_solution)
