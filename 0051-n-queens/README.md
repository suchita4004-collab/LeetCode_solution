# 0051 - N-Queens

## Problem

The **n-queens** puzzle is the problem of placing `n` queens on an `n x n` chessboard such that no two queens attack each other.

A queen can attack another queen if they are in the same:

- Row
- Column
- Diagonal

Given an integer `n`, return all distinct solutions to the n-queens puzzle.

Each solution is represented as a list of strings where:

- `Q` represents a queen.
- `.` represents an empty space.

## Examples

### Example 1

Input:
```text
n = 4
```

Output:
```text
[
[".Q..","...Q","Q...","..Q."],
["..Q.","Q...","...Q",".Q.."]
]
```

Explanation:

There are two distinct solutions for a 4 x 4 chessboard.

### Example 2

Input:
```text
n = 1
```

Output:
```text
[["Q"]]
```

Explanation:

There is only one position available, so the queen is placed in the only cell.

## Approach

We use **Backtracking** to solve the N-Queens problem.

The main idea is to place one queen in each row.

For every row, we try placing the queen in every possible column. Before placing it, we check whether the position is safe.

A position is safe if:

1. No other queen is in the same column.
2. No other queen is on the same diagonal.
3. No other queen is on the opposite diagonal.

To check these conditions efficiently, we use three sets:

```text
cols
diagonals1
diagonals2
```

### Column Check

For a cell `(row, col)`, the column is represented by:

```text
col
```

If `col` is already present in `cols`, another queen is already present in that column.

### First Diagonal

For one diagonal direction, cells have the same value of:

```text
row - col
```

Therefore, we store `row - col` in `diagonals1`.

### Second Diagonal

For the other diagonal direction, cells have the same value of:

```text
row + col
```

Therefore, we store `row + col` in `diagonals2`.

## Algorithm

1. Create an empty `n x n` chessboard.
2. Start placing queens from row `0`.
3. Try every column in the current row.
4. Check whether the position is safe.
5. If the position is safe:
   - Place the queen.
   - Add its column to `cols`.
   - Add `row - col` to `diagonals1`.
   - Add `row + col` to `diagonals2`.
6. Move to the next row using recursion.
7. If all `n` queens are placed:
   - Convert the board into strings.
   - Add the solution to the result.
8. Backtrack:
   - Remove the queen.
   - Remove the column and diagonal values from the sets.
9. Continue trying other positions.

## Solution

```text
class Solution:
    def solveNQueens(self, n):
        result = []
        board = [["."] * n for _ in range(n)]

        cols = set()
        diagonals1 = set()
        diagonals2 = set()

        def backtrack(row):
            if row == n:
                result.append(["".join(r) for r in board])
                return

            for col in range(n):
                if col in cols:
                    continue

                if row - col in diagonals1:
                    continue

                if row + col in diagonals2:
                    continue

                board[row][col] = "Q"
                cols.add(col)
                diagonals1.add(row - col)
                diagonals2.add(row + col)

                backtrack(row + 1)

                board[row][col] = "."
                cols.remove(col)
                diagonals1.remove(row - col)
                diagonals2.remove(row + col)

        backtrack(0)

        return result
```

## Dry Run

For:

```text
n = 4
```

Initially the board is:

```text
. . . .
. . . .
. . . .
. . . .
```

We start from row `0`.

Suppose we place a queen in column `1`:

```text
. Q . .
. . . .
. . . .
. . . .
```

Then we move to the next row and try another safe position.

After continuing the process, one valid solution is:

```text
. Q . .
. . . Q
Q . . .
. . Q .
```

Another valid solution is:

```text
. . Q .
Q . . .
. . . Q
. Q . .
```

Both solutions have four queens, and no two queens attack each other.

## Why Backtracking?

We cannot place queens randomly because a position that is safe for the current row may make it impossible to place queens in the remaining rows.

Backtracking allows us to:

- Try a possible position.
- Continue if the position is valid.
- Undo the choice if it does not lead to a solution.
- Try another position.

This helps us find all possible valid arrangements.

## Complexity

The time complexity is approximately:

```text
O(n!)
```

because we try different arrangements of queens and eliminate invalid positions using backtracking.

The board requires:

```text
O(n²)
```

space.

The sets used for columns and diagonals require:

```text
O(n)
```

auxiliary space.

The total space can also include the memory required to store all generated solutions.

## Key Concept

The main idea is **Backtracking**.

At every row:

```text
Try → Check → Place → Recurse → Undo
```

If a queen cannot be placed safely, we skip that position.

If a complete board is formed, we add it to the result.

## Constraints

- `1 <= n <= 9`

## Language

Python

## LeetCode Problem

Problem Number: **51**

Problem Name: **N-Queens**

Difficulty: **Hard**
