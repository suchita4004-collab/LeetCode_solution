# Maximal Rectangle

## Problem

You are given a binary matrix containing only `0`s and `1`s.

The task is to find the **largest rectangle containing only `1`s** and return its area.

For example:

```text
1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
```

The largest rectangle containing only `1`s has area:

```text
6
```

---

## Examples

### Example 1

**Input:**
```text
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
```

**Output:**
```text
6
```

### Example 2

**Input:**
```text
[["0"]]
```

**Output:**
```text
0
```

### Example 3

**Input:**
```text
[["1"]]
```

**Output:**
```text
1
```

---

## Approach

The main idea is to solve this problem using **Largest Rectangle in Histogram**, which was used in LeetCode #84.

For every row, we maintain an array called `heights`.

`heights[col]` tells us how many consecutive `1`s are present vertically up to the current row.

For example, consider:

```text
1 1 0 1
1 1 1 1
1 1 1 1
```

After processing each row, the histogram heights become:

```text
Row 1:
1 1 0 1

Row 2:
2 2 1 2

Row 3:
3 3 2 3
```

Each row now represents a histogram.

We then find the largest rectangle in that histogram using a **monotonic increasing stack**.

---

## Main Idea

The problem can be divided into two steps:

### Step 1: Build Histogram

For every `1`:

```text
heights[col] += 1
```

For every `0`:

```text
heights[col] = 0
```

### Step 2: Find Largest Histogram Rectangle

For every row, apply the same logic as **LeetCode #84 – Largest Rectangle in Histogram**.

Keep the largest area found across all rows.

---

## Algorithm

1. Check if the matrix is empty.
2. Create a `heights` array of size `cols`.
3. Set `max_area = 0`.
4. Process the matrix row by row.
5. For every column:
   - If the current cell is `1`, increase its height.
   - If the current cell is `0`, reset its height to `0`.
6. Treat `heights` as a histogram.
7. Use a monotonic increasing stack to find the largest rectangle.
8. Update `max_area`.
9. Repeat for every row.
10. Return `max_area`.

---

## Dry Run

Consider:

```text
1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
```

### Row 1

```text
1 0 1 0 0
```

Histogram:

```text
[1, 0, 1, 0, 0]
```

Largest area:

```text
1
```

---

### Row 2

```text
1 0 1 1 1
```

Update heights:

```text
[2, 0, 2, 1, 1]
```

The last three columns form:

```text
2 1 1
```

Largest area:

```text
3
```

---

### Row 3

```text
1 1 1 1 1
```

Update heights:

```text
[3, 1, 3, 2, 2]
```

Now consider:

```text
3 2 2
```

The height `2` can extend across three columns:

```text
Area = 2 × 3
     = 6
```

So:

```text
max_area = 6
```

---

### Row 4

```text
1 0 0 1 0
```

Update heights:

```text
[4, 0, 0, 3, 0]
```

No rectangle is larger than `6`.

Therefore:

```text
Output = 6
```

---

## Visual Understanding

For the input:

```text
1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
```

The largest rectangle is:

```text
1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
        ↑
```

The important area contains:

```text
1 1 1
1 1 1
```

So:

```text
Height = 2
Width  = 3

Area = 2 × 3
     = 6
```

---

## How the Code Works

### Create Heights Array

```python
heights = [0] * cols
```

Initially, every column has height `0`.

For a matrix with 5 columns:

```text
[0, 0, 0, 0, 0]
```

---

### Update Heights

```python
if matrix[row][col] == "1":
    heights[col] += 1
else:
    heights[col] = 0
```

If the cell is `1`, we increase the consecutive height.

If the cell is `0`, the consecutive sequence is broken, so the height becomes `0`.

---

### Create Stack

```python
stack = []
```

The stack stores indexes of bars in increasing order of height.

---

### Add a Virtual Zero

```python
for i in range(cols + 1):
    current_height = heights[i] if i < cols else 0
```

When `i == cols`, we use height `0`.

This acts like an extra zero-height bar and forces all remaining bars in the stack to be processed.

This is the same trick used in **LeetCode #84**.

---

### Calculate Rectangle

When a taller bar is removed from the stack:

```python
height = heights[stack.pop()]
```

We calculate its possible width:

```python
if stack:
    width = i - stack[-1] - 1
else:
    width = i
```

Then calculate:

```python
area = height * width
```

and update:

```python
max_area = max(max_area, area)
```

---

## Why This Approach Works

Every row represents the bottom of a possible rectangle.

The `heights` array tells us how far upward a column of `1`s extends.

For example:

```text
1 1 1
1 1 1
```

becomes:

```text
2 2 2
```

This is exactly a histogram.

Therefore, finding the largest rectangle of `1`s becomes the same problem as finding the largest rectangle in a histogram.

---

## Connection with LeetCode #84

This problem is directly related to:

**#84 – Largest Rectangle in Histogram**

### #84

Input:

```text
[2,1,5,6,2,3]
```

Find the largest rectangle in a histogram.

### #85

For every matrix row:

```text
Matrix
  ↓
Build histogram
  ↓
Largest Rectangle in Histogram
  ↓
Update maximum
```

So the main technique is:

```text
Binary Matrix
      ↓
Histogram for each row
      ↓
Monotonic Stack
      ↓
Largest Rectangle
```

---

## Important Edge Cases

### 1. Matrix Contains Only Zero

```text
Input:
[["0"]]

Output:
0
```

There is no rectangle containing `1`.

### 2. Matrix Contains Only One

```text
Input:
[["1"]]

Output:
1
```

The single cell itself is a rectangle.

### 3. All Ones

For:

```text
1 1
1 1
```

The largest rectangle is the complete matrix.

```text
Area = 2 × 2
     = 4
```

### 4. Single Row

```text
Input:
[["1","1","1","0"]]
```

The histogram is:

```text
[1,1,1,0]
```

Largest area:

```text
1 × 3 = 3
```

### 5. Single Column

```text
Input:
[["1"],
 ["1"],
 ["1"]]
```

Largest rectangle:

```text
Height = 3
Width = 1

Area = 3
```

---

## Complexity Analysis

Let:

```text
rows = number of rows
cols = number of columns
```

For every row, we process all columns once using the stack.

### Time Complexity

```text
O(rows × cols)
```

Each histogram bar is pushed and popped from the stack at most once.

### Space Complexity

```text
O(cols)
```

We store:

- `heights` array
- Stack

Both require at most `O(cols)` space.

---

## Key Concept

The main concepts used are:

- **Dynamic Histogram**
- **Monotonic Increasing Stack**
- **Largest Rectangle in Histogram**
- **Array Traversal**

The most important idea is:

> Convert every matrix row into a histogram and solve the histogram using a monotonic stack.

---

## Constraints

- `1 <= rows, cols <= 200`
- `matrix[i][j]` is either `'0'` or `'1'`.

Since the matrix can contain up to:

```text
200 × 200 = 40,000
```

cells, an `O(rows × cols)` solution is efficient.

---

## Language

**Python**

---

## LeetCode Information

- **Problem Number:** 85
- **Problem Name:** Maximal Rectangle
- **Difficulty:** Hard
- **Topics:** Array, Dynamic Programming, Stack, Matrix, Monotonic Stack

---

## File Structure

```text
LeetCode_solution/
│
└── 85-maximal-rectangle/
    ├── README.md
    └── solution.py
```

---

## Solution Link

[View Solution](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/85-maximal-rectangle/solution.py)

## Repository Link

[LeetCode_solution](https://github.com/suchita4004-collab/LeetCode_solution)
