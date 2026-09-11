# Word Search

## Problem

Given an `m x n` grid of characters `board` and a string `word`, determine whether the word exists in the grid.

The word can be formed using letters from **sequentially adjacent cells**.

A cell is adjacent to another cell if it is:

- Horizontally adjacent
- Vertically adjacent

The same cell **cannot be used more than once** while constructing the word.

Return:

- `True` if the word exists.
- `False` otherwise.

---

## Example 1

**Input:**

```text
board = [
    ["A", "B", "C", "E"],
    ["S", "F", "C", "S"],
    ["A", "D", "E", "E"]
]

word = "ABCCED"
```

**Output:**

```text
True
```

The word can be formed as:

```text
A → B → C
        ↓
        C
        ↓
        E → D
```

---

## Example 2

**Input:**

```text
board = [
    ["A", "B", "C", "E"],
    ["S", "F", "C", "S"],
    ["A", "D", "E", "E"]
]

word = "SEE"
```

**Output:**

```text
True
```

One valid path is:

```text
S
↓
E → E
```

---

## Example 3

**Input:**

```text
board = [
    ["A", "B", "C", "E"],
    ["S", "F", "C", "S"],
    ["A", "D", "E", "E"]
]

word = "ABCB"
```

**Output:**

```text
False
```

The required path cannot be completed without using a cell more than once.

---

## Approach

We use **Backtracking with Depth First Search (DFS)**.

For every cell in the board, we check whether it can be the starting point of the word.

If the first character matches, we explore its four possible directions:

```text
             Up
              ↑
              |
       Left ← Cell → Right
              |
              ↓
            Down
```

During the search, we temporarily mark a cell as visited.

After exploring that cell, we restore it so that it can be used in another possible path.

---

## Why Backtracking?

At every cell, there can be multiple possible directions.

For example:

```text
A → B → C
    ↓
    F
```

If one path does not work, we go back and try another path.

This is exactly what backtracking does:

```text
Choose
  ↓
Explore
  ↓
Success?
 /     \
Yes     No
 ↓       ↓
Return  Undo
          ↓
      Try another path
```

---

## Algorithm

1. Get the number of rows and columns.
2. Start from every cell in the board.
3. Check whether the cell contains the first character of `word`.
4. If it matches, start DFS/backtracking.
5. Check whether:
   - The cell is inside the board.
   - The character matches the current character of `word`.
6. Mark the cell as visited.
7. Explore:
   - Up
   - Down
   - Left
   - Right
8. If any direction finds the complete word, return `True`.
9. Restore the cell after exploration.
10. If no path works, return `False`.

---

## Dry Run

Consider:

```text
board = [
    ["A", "B", "C", "E"],
    ["S", "F", "C", "S"],
    ["A", "D", "E", "E"]
]

word = "ABCCED"
```

Start at:

```text
A
```

The first character matches.

### Step 1

Find:

```text
A
```

Mark it as visited.

Move right to:

```text
B
```

### Step 2

`B` matches the second character.

Move right to:

```text
C
```

### Step 3

`C` matches.

Move down to:

```text
C
```

### Step 4

The second `C` matches.

Move down:

```text
E
```

### Step 5

`E` matches.

Move left:

```text
D
```

### Step 6

`D` matches the final character.

Therefore:

```text
ABCCED
```

exists in the board.

Output:

```text
True
```

---

## How the Code Works

### 1. Get board dimensions

```python
rows = len(board)
cols = len(board[0])
```

These values are used to check whether a cell is inside the board.

---

### 2. Backtracking function

```python
def backtrack(row, col, index):
```

Here:

- `row` → current row
- `col` → current column
- `index` → current position in `word`

For example:

```text
word = "ABCCED"
```

If:

```text
index = 2
```

we are looking for:

```text
C
```

---

### 3. Check if the word is complete

```python
if index == len(word):
    return True
```

If we have matched every character, the word exists.

---

### 4. Check invalid cells

```python
if (row < 0 or row >= rows or
    col < 0 or col >= cols or
    board[row][col] != word[index]):
    return False
```

The search stops when:

- We move outside the board.
- The character does not match.
- The cell was already marked as visited.

---

### 5. Mark the cell as visited

```python
temp = board[row][col]
board[row][col] = "#"
```

We temporarily replace the character with `#`.

This prevents the same cell from being used again in the current path.

---

### 6. Explore four directions

```python
found = (
    backtrack(row + 1, col, index + 1) or
    backtrack(row - 1, col, index + 1) or
    backtrack(row, col + 1, index + 1) or
    backtrack(row, col - 1, index + 1)
)
```

The four calls represent:

```text
row + 1 → Down
row - 1 → Up
col + 1 → Right
col - 1 → Left
```

---

### 7. Restore the cell

```python
board[row][col] = temp
```

This is the **backtracking step**.

We restore the original character so that the cell can be used in another search path.

---

## Important Edge Cases

### Case 1: Single Cell

```text
board = [["A"]]
word = "A"
```

Output:

```text
True
```

---

### Case 2: Single Cell With Different Character

```text
board = [["A"]]
word = "B"
```

Output:

```text
False
```

---

### Case 3: Same Cell Cannot Be Reused

Suppose:

```text
board = [["A", "B"]]
word = "ABA"
```

The `A` cell cannot be used again.

Therefore, the word cannot be formed from these two cells.

---

### Case 4: Word Longer Than Available Cells

If:

```text
len(word) > rows × cols
```

the answer must be:

```text
False
```

because every cell can be used at most once.

---

### Case 5: Word Appears in Multiple Places

The algorithm checks every cell as a possible starting point.

So it can find the word regardless of where it begins.

---

## Complexity Analysis

Let:

- `m` = number of rows
- `n` = number of columns
- `L` = length of `word`

### Time Complexity

```text
O(m × n × 4^L)
```

In the worst case, we can start from every cell and explore up to four directions for each character.

Because we cannot reuse the previous cell, the practical branching factor after the first step is smaller, but `O(m × n × 4^L)` is a safe upper bound.

### Space Complexity

```text
O(L)
```

The recursion can go as deep as the length of the word.

The board is modified temporarily and restored, so no separate visited matrix is required.

---

## Key Concept

The main concepts used are:

**DFS + Backtracking**

The basic pattern is:

```text
Start from a cell
       ↓
Check character
       ↓
Mark as visited
       ↓
Explore 4 directions
       ↓
Found word?
    /      \
  Yes       No
   ↓         ↓
 Return    Restore
             ↓
         Try another path
```

The most important part of the code is:

```python
temp = board[row][col]
board[row][col] = "#"

found = (
    backtrack(row + 1, col, index + 1) or
    backtrack(row - 1, col, index + 1) or
    backtrack(row, col + 1, index + 1) or
    backtrack(row, col - 1, index + 1)
)

board[row][col] = temp
```

---

## Constraints

- `1 <= m, n <= 6`
- `1 <= word.length <= 15`
- `board` and `word` contain uppercase and lowercase English letters.
- The same cell cannot be used more than once.

---

## Language

**Python**

---

## LeetCode Information

- **Problem:** Word Search
- **Problem Number:** 79
- **Difficulty:** Medium
- **Topics:** Array, Backtracking, DFS, Matrix

---

## File Structure

```text
LeetCode_solution/
│
├── 79-word-search/
│   ├── solution.py
│   └── README.md
│
└── README.md
```

---

## Solution Link

[View Solution](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/79-word-search/solution.py)

## Repository Link

[LeetCode_solution](https://github.com/suchita4004-collab/LeetCode_solution)
