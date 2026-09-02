# Valid Parentheses

Given a string `s` containing only parentheses, determine whether the input string is valid.

A string is valid if every opening bracket is closed by the same type of bracket and the brackets are closed in the correct order.

## Example 1

```text
Input: s = "()"

Output: true
```

### Explanation

The opening `(` is correctly closed by `)`.

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/20-valid-parentheses/README.md#example-1)

## Example 2

```text
Input: s = "()[]{}"

Output: true
```

### Explanation

All brackets are correctly matched and closed in the proper order.

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/20-valid-parentheses/README.md#example-2)

## Example 3

```text
Input: s = "(]"

Output: false
```

### Explanation

`(` must be closed by `)`, but it is closed by `]`.

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/20-valid-parentheses/README.md#example-3)

## Example 4

```text
Input: s = "([])"

Output: true
```

### Explanation

The brackets are correctly nested:

`( [ ] )`

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/20-valid-parentheses/README.md#example-4)

## Example 5

```text
Input: s = "([)]"

Output: false
```

### Explanation

The brackets are not closed in the correct order.

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/20-valid-parentheses/README.md#example-5)

## Approach

We use a **stack** to keep track of opening brackets.

1. If the character is an opening bracket `(`, `{`, or `[`, push it into the stack.
2. If the character is a closing bracket, check the top element of the stack.
3. If the top element is the matching opening bracket, remove it from the stack.
4. If it does not match, return `False`.
5. At the end, the stack must be empty for the string to be valid.

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/20-valid-parentheses/README.md#approach)

## Complexity

* **Time Complexity:** O(n)
* **Space Complexity:** O(n)

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/20-valid-parentheses/README.md#complexity)

## Solution

[View Solution](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/20-valid-parentheses/solution.py)

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/20-valid-parentheses/README.md#solution)

## Folder Structure

```text
20-valid-parentheses/
├── README.md
└── solution.py
```
