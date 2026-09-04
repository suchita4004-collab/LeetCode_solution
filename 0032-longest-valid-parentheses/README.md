# Longest Valid Parentheses

## Problem

Given a string containing only `(` and `)`, find the length of the longest valid (well-formed) parentheses substring.

A valid parentheses string must have every opening parenthesis matched with a closing parenthesis in the correct order.

## Example 1

**Input**

```text
s = "(()"
```

### Output

```text
2
```

### Explanation

The longest valid parentheses substring is:

```text
()
```

Its length is `2`.

## Example 2

**Input**

```text
s = ")()())"
```

### Output

```text
4
```

### Explanation

The longest valid parentheses substring is:

```text
()()
```

Its length is `4`.

## Example 3

**Input**

```text
s = ""
```

### Output

```text
0
```

### Explanation

The input string is empty, so there is no valid parentheses substring.

## Approach

I use a **stack** to store the indices of unmatched parentheses.

Initially, I put `-1` in the stack. This acts as a starting boundary for calculating the length of a valid substring.

For each character:

1. If the character is `(`, store its index in the stack.
2. If the character is `)`, remove the top element from the stack.
3. If the stack becomes empty, store the current index as the new boundary.
4. Otherwise, calculate the current valid substring length using:

```text
current length = current index - stack[-1]
```

5. Keep track of the maximum length found.

The stack helps us identify the starting position of the current valid parentheses substring.

## Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

The string is scanned only once, and the stack can contain up to `n` indices.

## Solution

[View Solution](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/0032-longest-valid-parentheses/solution.py)

## Folder Structure

```text
0032-longest-valid-parentheses/
├── README.md
└── solution.py
```
