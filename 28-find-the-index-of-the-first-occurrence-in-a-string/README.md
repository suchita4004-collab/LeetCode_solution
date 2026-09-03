# Find the Index of the First Occurrence in a String

## Problem

Given two strings `needle` and `haystack`, return the index of the first occurrence of `needle` in `haystack`.

If `needle` is not part of `haystack`, return `-1`.

## Example 1

**Input**

```text id="h3t6kq"
haystack = "sadbutsad"
needle = "sad"
```

### Output

```text id="7ez7d3"
0
```

### Explanation

The string `"sad"` occurs at index `0` and index `6`.

The first occurrence is at index `0`, so we return `0`.

## Example 2

**Input**

```text id="z4x7kr"
haystack = "leetcode"
needle = "leeto"
```

### Output

```text id="v8x3q1"
-1
```

### Explanation

The string `"leeto"` is not present in `"leetcode"`.

Therefore, we return `-1`.

## Approach

I use Python's built-in string search operation to check whether `needle` is present in `haystack`.

If `needle` is found, I return the index of its first occurrence.

If it is not found, I return `-1`.

## Complexity

- Time Complexity: O(n × m)
- Space Complexity: O(1)

Where `n` is the length of `haystack` and `m` is the length of `needle`.

## Solution

[View Solution](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/28-find-the-index-of-the-first-occurrence-in-a-string/solution.py)

## Folder Structure

```text id="x7k2lm"
28-find-the-index-of-the-first-occurrence-in-a-string/
├── README.md
└── solution.py
```
