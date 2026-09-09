# 0062 - Unique Paths

## Problem

There is a robot on an `m x n` grid. The robot starts at the **top-left corner** of the grid and wants to reach the **bottom-right corner**.

The robot can move only in two directions:

- Right `→`
- Down `↓`

Given two integers `m` and `n`, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

---

## Examples

### Example 1

**Input:**
```text
m = 3
n = 7
```

**Output:**
```text
28
```

---

### Example 2

**Input:**
```text
m = 3
n = 2
```

**Output:**
```text
3
```

**Explanation:**

There are three possible paths:

```text
1. Right → Down → Down
2. Down → Down → Right
3. Down → Right → Down
```

---

## Approach

We solve this problem using **Dynamic Programming**.

For every cell in the grid, the robot can reach that cell from only two possible directions:

1. From the cell above.
2. From the cell on the left.

Therefore:

```text
dp[j] = dp[j] + dp[j - 1]
```

Where:

- `dp[j]` represents the number of ways to reach the current cell.
- `dp[j]` before updating represents the cell above.
- `dp[j - 1]` represents the cell on the left.

The first row has only one possible path because the robot can only move right.

Similarly, the first column has only one possible path because the robot can only move down.

---

## Algorithm

1. Create a 1D array `dp` of size `n`.
2. Initialize every element to `1`.
3. Traverse the grid from the second row.
4. For every column starting from the second column:
   - Add the number of paths from the left to the number of paths from above.
5. Return the last element of `dp`.

---

## Example Dry Run

Consider:

```text
m = 3
n = 3
```

Initially:

```text
dp = [1, 1, 1]
```

After processing the second row:

```text
dp = [1, 2, 3]
```

After processing the third row:

```text
dp = [1, 3, 6]
```

Therefore:

```text
Answer = 6
```

The complete DP table can be visualized as:

```text
1  1  1
1  2  3
1  3  6
```

So there are **6 unique paths**.

---

## Solution

```python
class Solution:
    def uniquePaths(self, m, n):
        dp = [1] * n

        for i in range(1, m):
            for j in range(1, n):
                dp[j] = dp[j] + dp[j - 1]

        return dp[n - 1]
```

---

## How the Code Works

### Step 1: Initialize DP

```python
dp = [1] * n
```

The first row has only one way to reach every cell, so all values are initialized to `1`.

For example:

```text
[1, 1, 1, 1, 1]
```

---

### Step 2: Traverse the Rows

```python
for i in range(1, m):
```

We start from the second row because the first row is already initialized.

---

### Step 3: Calculate Paths

```python
for j in range(1, n):
    dp[j] = dp[j] + dp[j - 1]
```

Here:

```text
dp[j]     → paths from above
dp[j - 1] → paths from left
```

Therefore:

```text
Current paths = Above + Left
```

---

### Step 4: Return the Answer

```python
return dp[n - 1]
```

The last element contains the number of ways to reach the bottom-right corner.

---

## Complexity Analysis

Let:

- `m` = number of rows
- `n` = number of columns

### Time Complexity

```text
O(m × n)
```

We visit every cell of the grid once.

### Space Complexity

```text
O(n)
```

We use only one 1D array of size `n`.

---

## Key Concept

The main idea is:

```text
Number of ways to reach a cell
=
Number of ways from above
+
Number of ways from left
```

In formula form:

```text
dp[i][j] = dp[i-1][j] + dp[i][j-1]
```

We optimize the 2D DP table into a 1D array to reduce memory usage.

---

## Alternative Approach

This problem can also be solved using **Combinations**.

To reach the bottom-right corner, the robot must make:

```text
m - 1 Down moves
n - 1 Right moves
```

Total moves:

```text
m + n - 2
```

Therefore, the answer is:

```text
C(m + n - 2, m - 1)
```

However, the Dynamic Programming solution is straightforward and easy to understand.

---

## Constraints

- `1 <= m, n <= 100`
- The answer is guaranteed to be less than or equal to `2 * 10^9`.

---

## Language

**Python**

---

## LeetCode

- **Problem:** 62 - Unique Paths
- **Difficulty:** Medium
- **Topic:** Dynamic Programming

---

## File Structure

```text
0062-unique-paths/
│
├── README.md
└── solution.py
```

### `README.md`

This file contains:

- Problem statement
- Examples
- Approach
- Algorithm
- Dry run
- Solution
- Complexity analysis
- Key concept
- Constraints

### `solution.py`

Contains the Python implementation:

```python
class Solution:
    def uniquePaths(self, m, n):
        dp = [1] * n

        for i in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j - 1]

        return dp[n - 1]
```

---

## GitHub Main README Entry

Add this row to your main repository `README.md`:

```markdown
| 62 | [Unique Paths](0062-unique-paths/) | Medium |
```

Your repository will then contain:

```text
LeetCode_solution/
│
├── 0001-two-sum/
├── 0002-add-two-numbers/
├── ...
├── 0051-n-queens/
├── 0052-n-queens-ii/
├── ...
└── 0062-unique-paths/
    ├── README.md
    └── solution.py
```v# 0062 - Unique Paths

## Problem

There is a robot on an `m x n` grid. The robot starts at the **top-left corner** of the grid and wants to reach the **bottom-right corner**.

The robot can move only in two directions:

- Right `→`
- Down `↓`

Given two integers `m` and `n`, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

---

## Examples

### Example 1

**Input:**
```text
m = 3
n = 7
```

**Output:**
```text
28
```

---

### Example 2

**Input:**
```text
m = 3
n = 2
```

**Output:**
```text
3
```

**Explanation:**

There are three possible paths:

```text
1. Right → Down → Down
2. Down → Down → Right
3. Down → Right → Down
```

---

## Approach

We solve this problem using **Dynamic Programming**.

For every cell in the grid, the robot can reach that cell from only two possible directions:

1. From the cell above.
2. From the cell on the left.

Therefore:

```text
dp[j] = dp[j] + dp[j - 1]
```

Where:

- `dp[j]` represents the number of ways to reach the current cell.
- `dp[j]` before updating represents the cell above.
- `dp[j - 1]` represents the cell on the left.

The first row has only one possible path because the robot can only move right.

Similarly, the first column has only one possible path because the robot can only move down.

---

## Algorithm

1. Create a 1D array `dp` of size `n`.
2. Initialize every element to `1`.
3. Traverse the grid from the second row.
4. For every column starting from the second column:
   - Add the number of paths from the left to the number of paths from above.
5. Return the last element of `dp`.

---

## Example Dry Run

Consider:

```text
m = 3
n = 3
```

Initially:

```text
dp = [1, 1, 1]
```

After processing the second row:

```text
dp = [1, 2, 3]
```

After processing the third row:

```text
dp = [1, 3, 6]
```

Therefore:

```text
Answer = 6
```

The complete DP table can be visualized as:

```text
1  1  1
1  2  3
1  3  6
```

So there are **6 unique paths**.

---

## Solution

```python
class Solution:
    def uniquePaths(self, m, n):
        dp = [1] * n

        for i in range(1, m):
            for j in range(1, n):
                dp[j] = dp[j] + dp[j - 1]

        return dp[n - 1]
```

---

## How the Code Works

### Step 1: Initialize DP

```python
dp = [1] * n
```

The first row has only one way to reach every cell, so all values are initialized to `1`.

For example:

```text
[1, 1, 1, 1, 1]
```

---

### Step 2: Traverse the Rows

```python
for i in range(1, m):
```

We start from the second row because the first row is already initialized.

---

### Step 3: Calculate Paths

```python
for j in range(1, n):
    dp[j] = dp[j] + dp[j - 1]
```

Here:

```text
dp[j]     → paths from above
dp[j - 1] → paths from left
```

Therefore:

```text
Current paths = Above + Left
```

---

### Step 4: Return the Answer

```python
return dp[n - 1]
```

The last element contains the number of ways to reach the bottom-right corner.

---

## Complexity Analysis

Let:

- `m` = number of rows
- `n` = number of columns

### Time Complexity

```text
O(m × n)
```

We visit every cell of the grid once.

### Space Complexity

```text
O(n)
```

We use only one 1D array of size `n`.

---

## Key Concept

The main idea is:

```text
Number of ways to reach a cell
=
Number of ways from above
+
Number of ways from left
```

In formula form:

```text
dp[i][j] = dp[i-1][j] + dp[i][j-1]
```

We optimize the 2D DP table into a 1D array to reduce memory usage.

---

## Alternative Approach

This problem can also be solved using **Combinations**.

To reach the bottom-right corner, the robot must make:

```text
m - 1 Down moves
n - 1 Right moves
```

Total moves:

```text
m + n - 2
```

Therefore, the answer is:

```text
C(m + n - 2, m - 1)
```

However, the Dynamic Programming solution is straightforward and easy to understand.

---

## Constraints

- `1 <= m, n <= 100`
- The answer is guaranteed to be less than or equal to `2 * 10^9`.

---

## Language

**Python**

---

## LeetCode

- **Problem:** 62 - Unique Paths
- **Difficulty:** Medium
- **Topic:** Dynamic Programming

---

## File Structure

```text
0062-unique-paths/
│
├── README.md
└── solution.py
```

### `README.md`

This file contains:

- Problem statement
- Examples
- Approach
- Algorithm
- Dry run
- Solution
- Complexity analysis
- Key concept
- Constraints

### `solution.py`

Contains the Python implementation:

```python
class Solution:
    def uniquePaths(self, m, n):
        dp = [1] * n

        for i in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j - 1]

        return dp[n - 1]
```

---

## GitHub Main README Entry

Add this row to your main repository `README.md`:

```markdown
| 62 | [Unique Paths](0062-unique-paths/) | Medium |
```

Your repository will then contain:

```text
LeetCode_solution/
│
├── 0001-two-sum/
├── 0002-add-two-numbers/
├── ...
├── 0051-n-queens/
├── 0052-n-queens-ii/
├── ...
└── 0062-unique-paths/
    ├── README.md
    └── solution.py
```
