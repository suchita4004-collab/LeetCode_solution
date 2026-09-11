```markdown id="q8m4xz"
# 74 - Search a 2D Matrix

## Problem

You are given an `m x n` integer matrix with the following properties:

- Each row is sorted in **non-decreasing order**.
- The first element of every row is greater than the last element of the previous row.

Because of these properties, the entire matrix can be treated like **one sorted array**.

Given an integer `target`, return:

- `true` if the target exists in the matrix.
- `false` if the target does not exist.

The solution must have:

```text
O(log(m * n))
```

time complexity.

---

## Examples

### Example 1

**Input:**
```text
matrix = [[1,3,5,7],
          [10,11,16,20],
          [23,30,34,60]]

target = 3
```

**Output:**
```text id="3o7m1b"
true
```

**Explanation:**

The value `3` exists in the matrix.

---

### Example 2

**Input:**
```text
matrix = [[1,3,5,7],
          [10,11,16,20],
          [23,30,34,60]]

target = 13
```

**Output:**
```text id="r4b2km"
false
```

**Explanation:**

The value `13` does not exist in the matrix.

---

## Approach

We can treat the entire matrix as a **single sorted array**.

For example:

```text id="2k8c7v"
1   3   5   7
10  11  16  20
23  30  34  60
```

Can be viewed as:

```text id="2x9t4s"
[1, 3, 5, 7, 10, 11, 16, 20, 23, 30, 34, 60]
```

Since this virtual array is sorted, we can use **Binary Search**.

---

## Why Binary Search?

The required time complexity is:

```text id="y6k3p8"
O(log(m * n))
```

Binary search is suitable because it reduces the search space by half in every step.

Instead of checking every element one by one, we directly check the middle element.

---

## Important Trick

Although the matrix is 2D, we use a single index:

```text id="j3d7sa"
mid
```

Then convert that index into a row and column.

### Row

```python id="m2n7xk"
row = mid // n
```

### Column

```python id="v8q4lc"
col = mid % n
```

For example, if:

```text id="7u5xj9"
n = 4
mid = 6
```

Then:

```text id="9a6k2v"
row = 6 // 4 = 1
col = 6 % 4 = 2
```

So the element is:

```text id="e7c3pz"
matrix[1][2]
```

---

## Algorithm

1. Find the number of rows `m`.
2. Find the number of columns `n`.
3. Consider the matrix as a virtual 1D sorted array of size `m * n`.
4. Set:
   ```text
   left = 0
   right = m * n - 1
   ```
5. Calculate the middle index.
6. Convert the middle index into row and column.
7. Compare the matrix element with `target`.
8. If equal, return `true`.
9. If the element is smaller than the target, search the right half.
10. Otherwise, search the left half.
11. If the search ends without finding the target, return `false`.

---

## Dry Run

Consider:

```text id="s3q2kv"
matrix = [[1,3,5,7],
          [10,11,16,20],
          [23,30,34,60]]

target = 3
```

There are:

```text id="5nqj8m"
m = 3
n = 4
```

Total elements:

```text id="0k7h6x"
3 × 4 = 12
```

Initial search range:

```text id="1z5j8p"
left = 0
right = 11
```

### Step 1

```text id="j5f4qy"
mid = (0 + 11) // 2
    = 5
```

Convert index `5`:

```text id="h4p9mc"
row = 5 // 4 = 1
col = 5 % 4 = 1
```

Element:

```text id="3s8k2p"
matrix[1][1] = 11
```

Since:

```text id="7q1v6z"
11 > 3
```

Search the left half.

```text id="w6x3k1"
right = 4
```

### Step 2

```text id="p2m7qa"
mid = (0 + 4) // 2
    = 2
```

Convert:

```text id="7y3k9d"
row = 2 // 4 = 0
col = 2 % 4 = 2
```

Element:

```text id="0r6m2x"
matrix[0][2] = 5
```

Since:

```text id="c4j8mz"
5 > 3
```

Search the left half.

```text id="a9v4sp"
right = 1
```

### Step 3

```text id="n6f2wd"
mid = (0 + 1) // 2
    = 0
```

Element:

```text id="8b5j3q"
matrix[0][0] = 1
```

Since:

```text id="k3s8wp"
1 < 3
```

Search the right half.

```text id="d7m2qa"
left = 1
```

### Step 4

```text id="x4p8nz"
mid = 1
```

Convert:

```text id="q6v3mb"
row = 1 // 4 = 0
col = 1 % 4 = 1
```

Element:

```text id="t8j5kc"
matrix[0][1] = 3
```

Target found!

```text id="v3k7qa"
Output = true
```

---

## Solution

```python id="q8x4mz"
class Solution:
    def searchMatrix(self, matrix, target):
        m = len(matrix)
        n = len(matrix[0])

        left = 0
        right = m * n - 1

        # Treat the matrix as one sorted array
        while left <= right:
            mid = (left + right) // 2

            # Convert 1D index to 2D row and column
            row = mid // n
            col = mid % n

            if matrix[row][col] == target:
                return True

            elif matrix[row][col] < target:
                left = mid + 1

            else:
                right = mid - 1

        return False
```

---

## How the Code Works

### 1. Get matrix dimensions

```python id="h3k9vs"
m = len(matrix)
n = len(matrix[0])
```

For example:

```text id="z2q6wy"
3 rows
4 columns
```

So there are:

```text id="m8v3qa"
3 × 4 = 12 elements
```

---

### 2. Set Binary Search boundaries

```python id="c7m4xp"
left = 0
right = m * n - 1
```

The virtual 1D array has indices:

```text id="j5w8ka"
0 1 2 3 4 5 6 7 8 9 10 11
```

---

### 3. Find the middle

```python id="x6q3nb"
mid = (left + right) // 2
```

This gives the middle position.

---

### 4. Convert 1D index to 2D index

```python id="p4v9sm"
row = mid // n
col = mid % n
```

This is the key idea of the solution.

For example:

```text id="7d2kqx"
mid = 9
n = 4

row = 9 // 4 = 2
col = 9 % 4 = 1
```

So:

```text id="k5m3vz"
matrix[2][1]
```

is the element we need to check.

---

### 5. Compare with target

If:

```python id="n8x4qm"
matrix[row][col] == target
```

return:

```text id="z4p6kc"
true
```

If the element is smaller:

```python id="c9v2sx"
left = mid + 1
```

Otherwise:

```python id="w5m7qa"
right = mid - 1
```

---

## Important Edge Cases

### Case 1: Target is the first element

```text id="p7m4xc"
matrix = [[1,3,5],
          [7,9,11]]

target = 1
```

Output:

```text id="f2q8vz"
true
```

---

### Case 2: Target is the last element

```text id="m5x9qa"
matrix = [[1,3,5],
          [7,9,11]]

target = 11
```

Output:

```text id="c8v2kp"
true
```

---

### Case 3: Target does not exist

```text id="y4n7sm"
matrix = [[1,3,5],
          [7,9,11]]

target = 6
```

Output:

```text id="r9x3wb"
false
```

---

### Case 4: Single element matrix

```text id="j6q2vn"
matrix = [[5]]
target = 5
```

Output:

```text id="k3m8zp"
true
```

---

### Case 5: Single row

```text id="v5s9cx"
matrix = [[1,3,5,7,9]]
target = 7
```

Output:

```text id="b2q6mw"
true
```

---

### Case 6: Single column

```text id="n7x4ka"
matrix = [[1],
          [3],
          [5],
          [7]]

target = 5
```

Output:

```text id="q8m2vz"
true
```

---

## Complexity Analysis

Let:

```text
m = number of rows
n = number of columns
```

### Time Complexity

```text
O(log(m × n))
```

Binary search checks approximately half of the remaining elements in every step.

### Space Complexity

```text
O(1)
```

Only a few variables are used.

No additional array or matrix is created.

---

## Key Concept

The main concept used in this problem is:

**Binary Search on a 2D Matrix**

The important trick is to treat the matrix as a virtual sorted 1D array.

```text
2D Matrix
    ↓
Virtual 1D Array
    ↓
Binary Search
    ↓
Convert index to row and column
```

The conversion is:

```text
row = index // number_of_columns
col = index % number_of_columns
```

---

## Constraints

```text
m == matrix.length
n == matrix[i].length

1 <= m, n <= 100

-10^4 <= matrix[i][j], target <= 10^4
```

---

## Language

**Python**

---

## LeetCode Information

- **Problem:** Search a 2D Matrix
- **Problem Number:** 74
- **Difficulty:** Medium
- **Topic:** Array / Binary Search
- **Pattern:** Binary Search

---

## File Structure

```text
74-search-a-2d-matrix/
├── README.md
└── solution.py
```

---

## Solution Link

[View Solution](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/74-search-a-2d-matrix/solution.py)

---

## Repository Link

[LeetCode_solution](https://github.com/suchita4004-collab/LeetCode_solution)
```
