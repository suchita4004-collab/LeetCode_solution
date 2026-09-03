# Generate Parentheses

## Problem

Given `n` pairs of parentheses, generate all combinations of well-formed parentheses.

A well-formed combination means that every opening parenthesis has a matching closing parenthesis and the parentheses are placed in the correct order.

## Example 1

**Input**

```text id="c8c8pg"
n = 3
```

### Output

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/22-generate-parentheses/README.md#output)

```text
["((()))","(()())","(())()","()(())","()()()"]
```

### Explanation

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/22-generate-parentheses/README.md#explanation)

For `n = 3`, we need exactly 3 opening and 3 closing parentheses.

The valid combinations are:

- `((()))`
- `(()())`
- `(())()`
- `()(())`
- `()()()`

## Example 2

**Input**

```text id="n3j8bh"
n = 1
```

### Output

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/22-generate-parentheses/README.md#output)

```text
["()"]
```

### Explanation

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/22-generate-parentheses/README.md#explanation)

For one pair of parentheses, the only valid combination is:

`()`

## Approach

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/22-generate-parentheses/README.md#approach)

I use **backtracking** to generate all valid combinations.

I keep track of the number of opening and closing parentheses used.

1. I can add an opening parenthesis if the number of opening parentheses is less than `n`.
2. I can add a closing parenthesis only when the number of closing parentheses is less than the number of opening parentheses.
3. This prevents invalid combinations such as `")("`.
4. When the length of the current string becomes `2 * n`, I add it to the result.

The backtracking process explores all possible valid combinations.

## Complexity

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/22-generate-parentheses/README.md#complexity)

- **Time Complexity:** O(4^n / √n)
- **Space Complexity:** O(4^n / √n)

The number of valid combinations is the `n`th Catalan number.

## Solution

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/22-generate-parentheses/README.md#solution)

[View Solution](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/22-generate-parentheses/solution.py)

## Folder Structure

```text id="k5m7dw"
22-generate-parentheses/
├── README.md
└── solution.py
```
