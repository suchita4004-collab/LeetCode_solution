# 37. Sudoku Solver

## Problem

Given a Sudoku puzzle, fill the empty cells so that the completed board satisfies all Sudoku rules.

The empty cells are represented by `"."`.

A valid Sudoku solution must satisfy:

1. Each row contains the digits `1-9` exactly once.
2. Each column contains the digits `1-9` exactly once.
3. Each `3 x 3` sub-box contains the digits `1-9` exactly once.

The input board is guaranteed to have exactly one solution.

## Example

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

**Output:**

```text
[
["5","3","4","6","7","8","9","1","2"],
["6","7","2","1","9","5","3","4","8"],
["1","9","8","3","4","2","5","6","7"],
["8","5","9","7","6","1","4","2","3"],
["4","2","6","8","5","3","7","9","1"],
["7","1","3","9","2","4","8","5","6"],
["9","6","1","5","3","7","2","8","4"],
["2","8","7","4","1","9","6","3","5"],
["3","4","5","2","8","6","1","7","9"]
]
```

## Approach

I use **backtracking** to solve the Sudoku puzzle.

First, I keep track of the numbers already used in:

- Each row
- Each column
- Each `3 x 3` box

For every empty cell:

1. Try each digit from `1` to `9`.
2. Check whether the digit can be placed in the current row, column, and `3 x 3` box.
3. If the digit is valid, place it in the cell.
4. Recursively solve the remaining empty cells.
5. If the choice does not lead to a solution, remove the digit and try another one.

When there are no empty cells left, the Sudoku is solved.

## Complexity

- Time Complexity: O(9^m), where `m` is the number of empty cells.
- Space Complexity: O(m)

The space is used by the recursion and the sets used to track the numbers.

## Solution

[View Solution](solution.py)
