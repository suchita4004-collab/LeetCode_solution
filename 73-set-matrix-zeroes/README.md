```markdown id="z7p3qa"
# 73 - Set Matrix Zeroes

## Problem

Given an `m x n` integer matrix, if any element is `0`, set its entire **row and column** to `0`.

The operation must be performed **in place**.

This means we should modify the original matrix instead of creating another matrix.

---

## Examples

### Example 1

**Input:**
```text
matrix = [[1,1,1],
          [1,0,1],
          [1,1,1]]
```

**Output:**
```text
[[1,0,1],
 [0,0,0],
 [1,0,1]]
```

**Explanation:**

The element at the center is `0`.

Therefore:

- Its entire row becomes `0`.
- Its entire column becomes `0`.

---

### Example 2

**Input:**
```text
matrix = [[0,1,2,0],
          [3,4,5,2],
          [1,3,1,5]]
```

**Output:**
```text
[[0,0,0,0],
 [0,4,5,0],
 [0,3,1,0]]
```

**Explanation:**

There are two zeros in the first row.

Therefore:

- The first row becomes zero.
- The first column becomes zero.
- The fourth column becomes zero.

---

## Approach

The straightforward approach is to create separate arrays for rows and columns that need to become zero.

But the follow-up asks for **constant extra space O(1)**.

To achieve this, we use the **first row and first column of the matrix as markers**.

When we find:

```text
matrix[i][j] == 0
```

we mark:

```text
matrix[i][0] = 0
matrix[0][j] = 0
```

This tells us that row `i` and column `j` must eventually become zero.

---

## Important Idea

The first row and first column are used to store information about which rows and columns should be zero.

For example:

```text
1  2  3  4
5  0  7  8
9  10 11 12
```

When we find `matrix[1][1] = 0`, we mark:

```text
matrix[1][0] = 0
matrix[0][1] = 0
```

The matrix becomes conceptually:

```text
1  0  3  4
0  0  7  8
9  10 11 12
```

The markers tell us:

- Row `1` → make zero
- Column `1` → make zero

---

## Why Do We Need `first_row_zero` and `first_col_zero`?

There is one special problem.

The first row and first column are being used as markers.

So if the first row originally contains a zero, we need to remember that separately.

We use:

```python
first_row_zero = False
first_col_zero = False
```

These are only two variables, so they use **constant space**.

---

## Algorithm

1. Check whether the first row contains a zero.
2. Check whether the first column contains a zero.
3. Traverse the matrix starting from row `1` and column `1`.
4. Whenever a zero is found:
   - Mark its row by setting `matrix[i][0] = 0`.
   - Mark its column by setting `matrix[0][j] = 0`.
5. Traverse the matrix again and set marked rows to zero.
6. Set marked columns to zero.
7. If the first row originally contained zero, make the entire first row zero.
8. If the first column originally contained zero, make the entire first column zero.

---

## Dry Run

Consider:

```text
matrix = [[1,1,1],
          [1,0,1],
          [1,1,1]]
```

### Step 1: Check first row

```text
[1, 1, 1]
```

No zero.

```text
first_row_zero = False
```

### Step 2: Check first column

```text
[1, 1, 1]
```

No zero.

```text
first_col_zero = False
```

### Step 3: Find zero

We find:

```text
matrix[1][1] = 0
```

Mark row `1`:

```text
matrix[1][0] = 0
```

Mark column `1`:

```text
matrix[0][1] = 0
```

Matrix becomes:

```text
1  0  1
0  0  1
1  1  1
```

### Step 4: Set marked row to zero

Row `1` is marked:

```text
0  0  0
```

### Step 5: Set marked column to zero

Column `1` is marked:

```text
1  0  1
0  0  0
1  0  1
```

Final result:

```text
[[1,0,1],
 [0,0,0],
 [1,0,1]]
```

---

## Solution

```python id="3g7w4p"
class Solution:
    def setZeroes(self, matrix):
        m = len(matrix)
        n = len(matrix[0])

        # Check if the first row contains a zero
        first_row_zero = False
        for j in range(n):
            if matrix[0][j] == 0:
                first_row_zero = True
                break

        # Check if the first column contains a zero
        first_col_zero = False
        for i in range(m):
            if matrix[i][0] == 0:
                first_col_zero = True
                break

        # Use first row and first column as markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Set marked rows to zero
        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(1, n):
                    matrix[i][j] = 0

        # Set marked columns to zero
        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(1, m):
                    matrix[i][j] = 0

        # Handle the first row
        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0

        # Handle the first column
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0
```

---

## How the Code Works

### 1. Get matrix dimensions

```python id="z8c0v5"
m = len(matrix)
n = len(matrix[0])
```

`m` represents the number of rows and `n` represents the number of columns.

---

### 2. Check the first row

```python id="j7x8c4"
first_row_zero = False

for j in range(n):
    if matrix[0][j] == 0:
        first_row_zero = True
        break
```

We remember whether the first row originally contained a zero.

---

### 3. Check the first column

```python id="s2q5pk"
first_col_zero = False

for i in range(m):
    if matrix[i][0] == 0:
        first_col_zero = True
        break
```

We remember whether the first column originally contained a zero.

---

### 4. Mark rows and columns

```python id="f3x7qm"
for i in range(1, m):
    for j in range(1, n):
        if matrix[i][j] == 0:
            matrix[i][0] = 0
            matrix[0][j] = 0
```

For every zero:

```text
matrix[i][0] = 0
```

marks the row.

```text
matrix[0][j] = 0
```

marks the column.

---

### 5. Set marked rows to zero

```python id="w4m8zs"
for i in range(1, m):
    if matrix[i][0] == 0:
        for j in range(1, n):
            matrix[i][j] = 0
```

If the first element of a row is zero, that row needs to be zeroed.

---

### 6. Set marked columns to zero

```python id="a9k1rf"
for j in range(1, n):
    if matrix[0][j] == 0:
        for i in range(1, m):
            matrix[i][j] = 0
```

If the first element of a column is zero, that column needs to be zeroed.

---

### 7. Handle first row

```python id="k3x6sd"
if first_row_zero:
    for j in range(n):
        matrix[0][j] = 0
```

If the first row originally contained a zero, make the entire row zero.

---

### 8. Handle first column

```python id="p6v2na"
if first_col_zero:
    for i in range(m):
        matrix[i][0] = 0
```

If the first column originally contained a zero, make the entire column zero.

---

## Important Edge Cases

### Case 1: Zero in the first row

```text
Input:
[[0,1,2],
 [3,4,5],
 [6,7,8]]
```

Output:

```text
[[0,0,0],
 [0,4,5],
 [0,7,8]]
```

---

### Case 2: Zero in the first column

```text
Input:
[[1,2,3],
 [0,5,6],
 [7,8,9]]
```

Output:

```text
[[0,2,3],
 [0,0,0],
 [0,8,9]]
```

---

### Case 3: All elements are zero

```text
Input:
[[0,0],
 [0,0]]
```

Output:

```text
[[0,0],
 [0,0]]
```

---

### Case 4: No zeros

```text
Input:
[[1,2],
 [3,4]]
```

Output:

```text
[[1,2],
 [3,4]]
```

Nothing changes.

---

## Complexity Analysis

### Time Complexity

```text
O(m × n)
```

We traverse the matrix a constant number of times.

### Space Complexity

```text
O(1)
```

We do not create another matrix, row array, or column array.

Only two boolean variables are used.

Therefore, this solution satisfies the **constant-space follow-up**.

---

## Key Concept

The main concept used in this problem is:

**In-place Matrix Manipulation**

The important trick is:

> Use the first row and first column as markers.

Instead of creating extra arrays, we store the information directly inside the input matrix.

---

## Comparison of Approaches

| Approach | Extra Space |
|----------|-------------|
| Separate matrix | O(m × n) |
| Row and column arrays | O(m + n) |
| First row/column markers | **O(1)** |

The third approach is the most space-efficient.

---

## Constraints

```text
m == matrix.length
n == matrix[0].length

1 <= m, n <= 200

-2^31 <= matrix[i][j] <= 2^31 - 1
```

---

## Language

**Python**

---

## LeetCode Information

- **Problem:** Set Matrix Zeroes
- **Problem Number:** 73
- **Difficulty:** Medium
- **Topic:** Array
- **Pattern:** In-place Matrix Manipulation

---

## File Structure

```text
73-set-matrix-zeroes/
├── README.md
└── solution.py
```

---

## Solution Link

[View Solution](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/73-set-matrix-zeroes/solution.py)

---

## Repository Link

[LeetCode_solution](https://github.com/suchita4004-collab/LeetCode_solution)
``````markdown id="z7p3qa"
# 73 - Set Matrix Zeroes

## Problem

Given an `m x n` integer matrix, if any element is `0`, set its entire **row and column** to `0`.

The operation must be performed **in place**.

This means we should modify the original matrix instead of creating another matrix.

---

## Examples

### Example 1

**Input:**
```text
matrix = [[1,1,1],
          [1,0,1],
          [1,1,1]]
```

**Output:**
```text
[[1,0,1],
 [0,0,0],
 [1,0,1]]
```

**Explanation:**

The element at the center is `0`.

Therefore:

- Its entire row becomes `0`.
- Its entire column becomes `0`.

---

### Example 2

**Input:**
```text
matrix = [[0,1,2,0],
          [3,4,5,2],
          [1,3,1,5]]
```

**Output:**
```text
[[0,0,0,0],
 [0,4,5,0],
 [0,3,1,0]]
```

**Explanation:**

There are two zeros in the first row.

Therefore:

- The first row becomes zero.
- The first column becomes zero.
- The fourth column becomes zero.

---

## Approach

The straightforward approach is to create separate arrays for rows and columns that need to become zero.

But the follow-up asks for **constant extra space O(1)**.

To achieve this, we use the **first row and first column of the matrix as markers**.

When we find:

```text
matrix[i][j] == 0
```

we mark:

```text
matrix[i][0] = 0
matrix[0][j] = 0
```

This tells us that row `i` and column `j` must eventually become zero.

---

## Important Idea

The first row and first column are used to store information about which rows and columns should be zero.

For example:

```text
1  2  3  4
5  0  7  8
9  10 11 12
```

When we find `matrix[1][1] = 0`, we mark:

```text
matrix[1][0] = 0
matrix[0][1] = 0
```

The matrix becomes conceptually:

```text
1  0  3  4
0  0  7  8
9  10 11 12
```

The markers tell us:

- Row `1` → make zero
- Column `1` → make zero

---

## Why Do We Need `first_row_zero` and `first_col_zero`?

There is one special problem.

The first row and first column are being used as markers.

So if the first row originally contains a zero, we need to remember that separately.

We use:

```python
first_row_zero = False
first_col_zero = False
```

These are only two variables, so they use **constant space**.

---

## Algorithm

1. Check whether the first row contains a zero.
2. Check whether the first column contains a zero.
3. Traverse the matrix starting from row `1` and column `1`.
4. Whenever a zero is found:
   - Mark its row by setting `matrix[i][0] = 0`.
   - Mark its column by setting `matrix[0][j] = 0`.
5. Traverse the matrix again and set marked rows to zero.
6. Set marked columns to zero.
7. If the first row originally contained zero, make the entire first row zero.
8. If the first column originally contained zero, make the entire first column zero.

---

## Dry Run

Consider:

```text
matrix = [[1,1,1],
          [1,0,1],
          [1,1,1]]
```

### Step 1: Check first row

```text
[1, 1, 1]
```

No zero.

```text
first_row_zero = False
```

### Step 2: Check first column

```text
[1, 1, 1]
```

No zero.

```text
first_col_zero = False
```

### Step 3: Find zero

We find:

```text
matrix[1][1] = 0
```

Mark row `1`:

```text
matrix[1][0] = 0
```

Mark column `1`:

```text
matrix[0][1] = 0
```

Matrix becomes:

```text
1  0  1
0  0  1
1  1  1
```

### Step 4: Set marked row to zero

Row `1` is marked:

```text
0  0  0
```

### Step 5: Set marked column to zero

Column `1` is marked:

```text
1  0  1
0  0  0
1  0  1
```

Final result:

```text
[[1,0,1],
 [0,0,0],
 [1,0,1]]
```

---

## Solution

```python id="3g7w4p"
class Solution:
    def setZeroes(self, matrix):
        m = len(matrix)
        n = len(matrix[0])

        # Check if the first row contains a zero
        first_row_zero = False
        for j in range(n):
            if matrix[0][j] == 0:
                first_row_zero = True
                break

        # Check if the first column contains a zero
        first_col_zero = False
        for i in range(m):
            if matrix[i][0] == 0:
                first_col_zero = True
                break

        # Use first row and first column as markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Set marked rows to zero
        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(1, n):
                    matrix[i][j] = 0

        # Set marked columns to zero
        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(1, m):
                    matrix[i][j] = 0

        # Handle the first row
        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0

        # Handle the first column
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0
```

---

## How the Code Works

### 1. Get matrix dimensions

```python id="z8c0v5"
m = len(matrix)
n = len(matrix[0])
```

`m` represents the number of rows and `n` represents the number of columns.

---

### 2. Check the first row

```python id="j7x8c4"
first_row_zero = False

for j in range(n):
    if matrix[0][j] == 0:
        first_row_zero = True
        break
```

We remember whether the first row originally contained a zero.

---

### 3. Check the first column

```python id="s2q5pk"
first_col_zero = False

for i in range(m):
    if matrix[i][0] == 0:
        first_col_zero = True
        break
```

We remember whether the first column originally contained a zero.

---

### 4. Mark rows and columns

```python id="f3x7qm"
for i in range(1, m):
    for j in range(1, n):
        if matrix[i][j] == 0:
            matrix[i][0] = 0
            matrix[0][j] = 0
```

For every zero:

```text
matrix[i][0] = 0
```

marks the row.

```text
matrix[0][j] = 0
```

marks the column.

---

### 5. Set marked rows to zero

```python id="w4m8zs"
for i in range(1, m):
    if matrix[i][0] == 0:
        for j in range(1, n):
            matrix[i][j] = 0
```

If the first element of a row is zero, that row needs to be zeroed.

---

### 6. Set marked columns to zero

```python id="a9k1rf"
for j in range(1, n):
    if matrix[0][j] == 0:
        for i in range(1, m):
            matrix[i][j] = 0
```

If the first element of a column is zero, that column needs to be zeroed.

---

### 7. Handle first row

```python id="k3x6sd"
if first_row_zero:
    for j in range(n):
        matrix[0][j] = 0
```

If the first row originally contained a zero, make the entire row zero.

---

### 8. Handle first column

```python id="p6v2na"
if first_col_zero:
    for i in range(m):
        matrix[i][0] = 0
```

If the first column originally contained a zero, make the entire column zero.

---

## Important Edge Cases

### Case 1: Zero in the first row

```text
Input:
[[0,1,2],
 [3,4,5],
 [6,7,8]]
```

Output:

```text
[[0,0,0],
 [0,4,5],
 [0,7,8]]
```

---

### Case 2: Zero in the first column

```text
Input:
[[1,2,3],
 [0,5,6],
 [7,8,9]]
```

Output:

```text
[[0,2,3],
 [0,0,0],
 [0,8,9]]
```

---

### Case 3: All elements are zero

```text
Input:
[[0,0],
 [0,0]]
```

Output:

```text
[[0,0],
 [0,0]]
```

---

### Case 4: No zeros

```text
Input:
[[1,2],
 [3,4]]
```

Output:

```text
[[1,2],
 [3,4]]
```

Nothing changes.

---

## Complexity Analysis

### Time Complexity

```text
O(m × n)
```

We traverse the matrix a constant number of times.

### Space Complexity

```text
O(1)
```

We do not create another matrix, row array, or column array.

Only two boolean variables are used.

Therefore, this solution satisfies the **constant-space follow-up**.

---

## Key Concept

The main concept used in this problem is:

**In-place Matrix Manipulation**

The important trick is:

> Use the first row and first column as markers.

Instead of creating extra arrays, we store the information directly inside the input matrix.

---

## Comparison of Approaches

| Approach | Extra Space |
|----------|-------------|
| Separate matrix | O(m × n) |
| Row and column arrays | O(m + n) |
| First row/column markers | **O(1)** |

The third approach is the most space-efficient.

---

## Constraints

```text
m == matrix.length
n == matrix[0].length

1 <= m, n <= 200

-2^31 <= matrix[i][j] <= 2^31 - 1
```

---

## Language

**Python**

---

## LeetCode Information

- **Problem:** Set Matrix Zeroes
- **Problem Number:** 73
- **Difficulty:** Medium
- **Topic:** Array
- **Pattern:** In-place Matrix Manipulation

---

## File Structure

```text
73-set-matrix-zeroes/
├── README.md
└── solution.py
```

---

## Solution Link

[View Solution](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/73-set-matrix-zeroes/solution.py)

---

## Repository Link

[LeetCode_solution](https://github.com/suchita4004-collab/LeetCode_solution)
```****
