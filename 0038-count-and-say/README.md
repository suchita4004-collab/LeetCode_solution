# 38. Count and Say

## Problem

The **count-and-say** sequence is a sequence of digit strings defined as:

- `countAndSay(1) = "1"`
- `countAndSay(n)` is the run-length encoding of `countAndSay(n - 1)`.

Run-length encoding means counting consecutive identical digits and writing the count followed by the digit.

For example:

```text
"3322251"
```

can be described as:

```text
"two 3s, three 2s, one 5, one 1"
```

So the result is:

```text
"23321511"
```

## Example 1

**Input:** `n = 4`

**Output:** `"1211"`

### Explanation

```text
countAndSay(1) = "1"
countAndSay(2) = "11"
countAndSay(3) = "21"
countAndSay(4) = "1211"
```

## Example 2

**Input:** `n = 1`

**Output:** `"1"`

### Explanation

This is the base case.

## Approach

I start with the string `"1"`.

For every step from `2` to `n`, I read the current string from left to right.

I count consecutive identical digits. When the digit changes, I add the count followed by the digit to the result.

For example:

```text
"21"
```

contains:

```text
one 2 → "12"
one 1 → "11"
```

So the next string is:

```text
"1211"
```

I repeat this process until I reach the required `n`.

## Complexity

- Time Complexity: O(n × m), where `m` is the length of the generated string.
- Space Complexity: O(m)

The generated string is stored for each step.

## Solution

[View Solution](solution.py)
