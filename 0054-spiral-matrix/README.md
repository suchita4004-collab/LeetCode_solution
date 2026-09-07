# 0054 - Spiral Matrix

## Problem

Given an `m x n` matrix, return all elements of the matrix in **spiral order**.

Spiral order means traversing the matrix:

1. From left to right
2. From top to bottom
3. From right to left
4. From bottom to top

Then repeat the process for the remaining inner matrix.

## Examples

### Example 1

Input:

```text
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
```

Output:

```text
[1,2,3,6,9,8,7,4,5]
```

Explanation:

The elements are visited in this order:

```text
1 → 2 → 3 → 6 → 9 → 8 → 7 → 4 → 5
```

### Example 2

Input:

```text
matrix = [[1,2,3,4],
          [5,6,7,8],
          [9,10,11,12]]
```

Output:

```text
[1,2,3,4,8,12,11,10,9,5,6,7]
```

## Approach

We use **four boundaries** to keep track of the part of the matrix that has not been visited yet.

The four boundaries are:

- `top` - first unvisited row
- `bottom` - last unvisited row
- `left` - first unvisited column
- `right` - last unvisited column

For every round, we traverse four directions.

### 1. Left to Right

Traverse the top row from `left` to `right`.

After visiting it, move the `top` boundary down:

```text
top += 1
```

### 2. Top to Bottom

Traverse the right column from `top` to `bottom`.

After visiting it, move the `right` boundary left:

```text
right -= 1
```

### 3. Right to Left

Traverse the bottom row from `right` to `left`.

After visiting it, move the `bottom` boundary up:

```text
bottom -= 1
```

This traversal is performed only if:

```text
top <= bottom
```

### 4. Bottom to Top

Traverse the left column from `bottom` to `top`.

After visiting it, move the `left` boundary right:

```text
left += 1
```

This traversal is performed only if:

```text
left <= right
```

We continue until all elements have been visited.

## Algorithm

1. Create an empty list `result`.
2. Initialize:
   - `top = 0`
   - `bottom = len(matrix) - 1`
   - `left = 0`
   - `right = len(matrix[0]) - 1`
3. While `top <= bottom` and `left <= right`:
   - Traverse the top row from left to right.
   - Move `top` down.
   - Traverse the right column from top to bottom.
   - Move `right` left.
   - If rows remain, traverse the bottom row from right to left.
   - Move `bottom` up.
   - If columns remain, traverse the left column from bottom to top.
   - Move `left` right.
4. Return `result`.

## Solution

```python
class Solution:
    def spiralOrder(self, matrix):
        result = []

        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1

        while top <= bottom and left <= right:

            # Left to right
            for col in range(left, right + 1):
                result.append(matrix[top][col])
            top += 1

            # Top to bottom
            for row in range(top, bottom + 1):
                result.append(matrix[row][right])
            right -= 1

            # Right to left
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    result.append(matrix[bottom][col])
                bottom -= 1

            # Bottom to top
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    result.append(matrix[row][left])
                left += 1

        return result
```

## Dry Run

Consider:

```text
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
```

Initially:

```text
top = 0
bottom = 2
left = 0
right = 2
```

### Step 1: Left to Right

Visit:

```text
1  2  3
```

Result:

```text
[1,2,3]
```

Now:

```text
top = 1
```

### Step 2: Top to Bottom

Visit:

```text
6
9
```

Result:

```text
[1,2,3,6,9]
```

Now:

```text
right = 1
```

### Step 3: Right to Left

Visit:

```text
8  7
```

Result:

```text
[1,2,3,6,9,8,7]
```

Now:

```text
bottom = 1
```

### Step 4: Bottom to Top

Visit:

```text
4
```

Result:

```text
[1,2,3,6,9,8,7,4]
```

Now:

```text
left = 1
```

Only the center element remains:

```text
5
```

Final result:

```text
[1,2,3,6,9,8,7,4,5]
```

## Why Do We Use Four Boundaries?

The four boundaries make it easy to know which part of the matrix has already been visited.

```text
        left       right
          ↓          ↓
top →    1  2  3
         4  5  6
bottom → 7  8  9
```

After completing each side, we move the corresponding boundary inward.

This prevents visiting the same element more than once.

## Complexity

Let the matrix contain `m × n` elements.

- **Time Complexity:** `O(m × n)`
- **Space Complexity:** `O(m × n)`

The output list contains all matrix elements, so `O(m × n)` space is required for the returned result.

Apart from the output, the algorithm uses only `O(1)` extra working space.

## Key Concept

The main concept used in this problem is **Boundary Traversal**.

The four boundaries are:

```text
top
bottom
left
right
```

They shrink toward the center after every complete spiral layer.

## Constraints

- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= m, n <= 10`
- `-100 <= matrix[i][j] <= 100`

## Language

Python

## LeetCode Problem

Problem Number: **54**

Problem Name: **Spiral Matrix**

Difficulty: **Medium**
