# 0059 - Spiral Matrix II

## Problem

Given a positive integer `n`, generate an `n x n` matrix filled with elements from `1` to `n²` in **spiral order**.

The spiral starts from the top-left corner and moves:

1. Left to right
2. Top to bottom
3. Right to left
4. Bottom to top

This process continues toward the center of the matrix.

## Examples

### Example 1

**Input:**
```text
n = 3
```

**Output:**
```text
[[1,2,3],
 [8,9,4],
 [7,6,5]]
```

### Example 2

**Input:**
```text
n = 1
```

**Output:**
```text
[[1]]
```

## Approach

We use the **Boundary Simulation** approach.

We maintain four boundaries:

- `top` - represents the top row
- `bottom` - represents the bottom row
- `left` - represents the left column
- `right` - represents the right column

We fill the matrix layer by layer.

For every layer, we perform four operations:

1. Fill the top row from left to right.
2. Fill the right column from top to bottom.
3. Fill the bottom row from right to left.
4. Fill the left column from bottom to top.

After each operation, the corresponding boundary is moved inward.

The process continues until the entire matrix is filled.

## Algorithm

1. Create an `n x n` matrix filled with `0`.
2. Initialize:
   ```text
   top = 0
   bottom = n - 1
   left = 0
   right = n - 1
   ```
3. Set `num = 1`.
4. While `top <= bottom` and `left <= right`:
   - Fill the top row.
   - Increase `top`.
   - Fill the right column.
   - Decrease `right`.
   - Fill the bottom row if the boundaries are valid.
   - Decrease `bottom`.
   - Fill the left column if the boundaries are valid.
   - Increase `left`.
5. Return the completed matrix.

## Solution

```python
class Solution:
    def generateMatrix(self, n):
        matrix = [[0] * n for _ in range(n)]

        top = 0
        bottom = n - 1
        left = 0
        right = n - 1

        num = 1

        while top <= bottom and left <= right:

            # Fill top row
            for col in range(left, right + 1):
                matrix[top][col] = num
                num += 1

            top += 1

            # Fill right column
            for row in range(top, bottom + 1):
                matrix[row][right] = num
                num += 1

            right -= 1

            # Fill bottom row
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    matrix[bottom][col] = num
                    num += 1

                bottom -= 1

            # Fill left column
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    matrix[row][left] = num
                    num += 1

                left += 1

        return matrix
```

## Dry Run

For:

```text
n = 3
```

Initially:

```text
0 0 0
0 0 0
0 0 0
```

### Step 1 - Fill Top Row

```text
1 2 3
0 0 0
0 0 0
```

### Step 2 - Fill Right Column

```text
1 2 3
0 0 4
0 0 5
```

### Step 3 - Fill Bottom Row

```text
1 2 3
0 0 4
7 6 5
```

### Step 4 - Fill Left Column

```text
1 2 3
8 0 4
7 6 5
```

### Step 5 - Fill Center

```text
1 2 3
8 9 4
7 6 5
```

Therefore:

```text
[[1,2,3],
 [8,9,4],
 [7,6,5]]
```

## Why This Approach Works

At every stage, the four boundaries represent the part of the matrix that has not been filled yet.

After filling one complete layer, the boundaries move inward.

For example:

```text
→ → →
↑     ↓
↑     ↓
← ← ←
```

The same process is repeated for the inner layers until every position contains exactly one number.

This guarantees that the numbers from `1` to `n²` are placed in clockwise spiral order.

## Complexity Analysis

The matrix contains `n²` cells, and every cell is filled exactly once.

- **Time Complexity:** `O(n²)`
- **Space Complexity:** `O(n²)`

The `O(n²)` space is required for the output matrix itself.

## Edge Cases

### Case 1: `n = 1`

Input:

```text
n = 1
```

Output:

```text
[[1]]
```

### Case 2: `n = 2`

Output:

```text
[[1,2],
 [4,3]]
```

### Case 3: Odd-sized matrix

For example, `n = 3`, the final remaining cell is the center:

```text
[9]
```

## Constraints

- `1 <= n <= 20`

## Language

**Python**

## LeetCode Information

- **Problem Number:** 59
- **Problem Name:** Spiral Matrix II
- **Difficulty:** Medium
- **Topics:** Array, Matrix, Simulation

## Solution Link

[LeetCode - Spiral Matrix II](https://leetcode.com/problems/spiral-matrix-ii/)

## Repository Structure

```text
LeetCode_solution/
│
├── 0001-two-sum/
├── 0002-add-two-numbers/
├── ...
├── 0058-length-of-last-word/
│
└── 0059-spiral-matrix-ii/
    ├── README.md
    └── solution.py
```

## Key Concept

The main concept used in this problem is **Matrix Simulation with Four Boundaries**.

```text
top
 ↓
[  → → →  ]
[  ↑   ↓  ]
[  ↑ ← ←  ]
```

By shrinking `top`, `bottom`, `left`, and `right` after each layer, we can efficiently construct the spiral matrix.
