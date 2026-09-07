# 0052 - N-Queens II

## Problem

The **N-Queens** puzzle is the problem of placing `n` queens on an `n x n` chessboard such that no two queens attack each other.

Given an integer `n`, return the **number of distinct solutions** to the N-Queens puzzle.

A queen can attack another queen if they are in the same:

- Row
- Column
- Diagonal

## Examples

### Example 1

Input:
```text
n = 4
```

Output:
```text
2
```

Explanation:

There are two distinct solutions for a 4 × 4 chessboard.

### Example 2

Input:
```text
n = 1
```

Output:
```text
1
```

Explanation:

There is only one possible position for the queen.

## Approach

We use **Backtracking** to solve this problem.

The idea is to place one queen in each row. For every row, we try placing the queen in each column.

Before placing a queen, we check whether that position is safe.

A position is safe if:

1. The column does not already contain a queen.
2. The main diagonal does not contain a queen.
3. The anti-diagonal does not contain a queen.

If the position is safe, we place the queen and move to the next row.

If no valid position is available, we **backtrack** by removing the previously placed queen and trying another position.

When all `n` rows have a queen, we have found one valid solution, so we increase the count.

## Important Diagonal Concept

For a cell `(row, col)`:

### Main Diagonal

Cells on the same main diagonal have the same:

```text
row - col
```

### Anti-Diagonal

Cells on the same anti-diagonal have the same:

```text
row + col
```

Therefore, we can use sets to keep track of:

```text
columns
row - col
row + col
```

This allows us to check whether a queen can be placed in constant time.

## Algorithm

1. Create three sets:
   - `cols` for occupied columns.
   - `diag1` for occupied main diagonals.
   - `diag2` for occupied anti-diagonals.
2. Start placing queens from row `0`.
3. Try every column in the current row.
4. Check whether the column and diagonals are free.
5. If safe:
   - Add the column and diagonals to their sets.
   - Place the queen.
   - Recursively process the next row.
6. After returning from recursion:
   - Remove the column and diagonal values.
   - This is the backtracking step.
7. When `row == n`, one complete solution is found.
8. Return the total number of solutions.

## Solution

```python
class Solution:
    def totalNQueens(self, n):
        cols = set()
        diag1 = set()
        diag2 = set()

        count = 0

        def backtrack(row):
            nonlocal count

            if row == n:
                count += 1
                return

            for col in range(n):
                if col in cols:
                    continue

                if row - col in diag1:
                    continue

                if row + col in diag2:
                    continue

                # Place queen
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)

                backtrack(row + 1)

                # Remove queen - backtracking
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

        backtrack(0)

        return count
```

## Dry Run

For:

```text
n = 4
```

We start from row `0`.

Possible positions are checked one by one.

For example, placing a queen at:

```text
(row, col) = (0, 0)
```

means:

```text
column = 0
row - col = 0
row + col = 0
```

These positions are marked as occupied.

Then we move to row `1`.

If a position conflicts with an existing queen, it is skipped.

If no valid position is available, we go back to the previous row and move that queen to another column.

This process continues until all possible arrangements are checked.

For `n = 4`, the algorithm finds:

```text
2
```

valid arrangements.

Therefore:

```text
Output = 2
```

## Why Backtracking?

Trying every possible arrangement would be very expensive.

Backtracking avoids unnecessary work.

Whenever a queen cannot be placed safely, we immediately stop exploring that arrangement instead of continuing further.

This makes the solution much more efficient.

## Complexity

The worst-case time complexity is approximately:

```text
O(N!)
```

because we try different arrangements of queens across the rows.

The space complexity is:

```text
O(N)
```

for the sets and recursion stack.

## Key Concepts

The main concepts used in this problem are:

- **Backtracking**
- **Recursion**
- **Sets**
- **Column checking**
- **Diagonal checking**

The most important condition is:

```python
row - col
```

for one diagonal and:

```python
row + col
```

for the other diagonal.

## Constraints

- `1 <= n <= 9`

## Language

Python

## LeetCode Problem

Problem Number: **52**

Problem Name: **N-Queens II**

Difficulty: **Hard**
