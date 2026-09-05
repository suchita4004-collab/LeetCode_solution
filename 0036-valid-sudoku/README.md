# 36. Valid Sudoku

## Problem

Given a `9 x 9` Sudoku board, determine whether it is valid.

Only the filled cells need to be checked.

The board is valid if:

1. Each row contains the digits `1-9` without repetition.
2. Each column contains the digits `1-9` without repetition.
3. Each `3 x 3` sub-box contains the digits `1-9` without repetition.

An empty cell is represented by `"."`.

## Example 1

**Input:**

```text
board = [
["5","3",".",".","7",".",".",".","."],
["6",".",".","1","9","5",".",".","."],
[".","9","8",".",".",".",".","6","."],
["8",".",".",".","6",".",".",".","3"],
["4",".",".","8",".","3",".",".","1"],
["7",".",".",".","2",".",".",".","6"],
[".","6",".",".",".",".","2","8","."],
[".",".",".","4","1","9",".",".","5"],
[".",".",".",".","8",".",".","7","9"]
]
```

**Output:** `true`

## Example 2

**Input:**

```text
board = [
["8","3",".",".","7",".",".",".","."],
["6",".",".","1","9","5",".",".","."],
[".","9","8",".",".",".",".","6","."],
["8",".",".",".","6",".",".",".","3"],
["4",".",".","8",".","3",".",".","1"],
["7",".",".",".","2",".",".",".","6"],
[".","6",".",".",".",".","2","8","."],
[".",".",".","4","1","9",".",".","5"],
[".",".",".",".","8",".",".","7","9"]
]
```

**Output:** `false`

### Explanation

The value `8` appears twice in the top-left `3 x 3` sub-box, so the Sudoku board is invalid.

## Approach

I use three sets to keep track of the numbers already seen:

- `rows` stores numbers present in each row.
- `cols` stores numbers present in each column.
- `boxes` stores numbers present in each `3 x 3` sub-box.

For every filled cell:

1. Check whether the number is already present in its row.
2. Check whether it is already present in its column.
3. Check whether it is already present in its `3 x 3` box.
4. If it appears in any of them, return `False`.
5. Otherwise, add it to the corresponding sets.

The box number is calculated using:

```text
box_index = (row // 3) * 3 + (col // 3)
```

If all filled cells pass the checks, return `True`.

## Complexity

- Time Complexity: O(1)
- Space Complexity: O(1)

The board always has exactly `81` cells, so the amount of work and extra storage is bounded by a constant.

## Solution

[View Solution](solution.py)
