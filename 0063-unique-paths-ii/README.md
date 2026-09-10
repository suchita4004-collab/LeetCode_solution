# 0063 - Unique Paths II

## Problem

You are given an `m x n` grid where:

- `0` represents an empty cell.
- `1` represents an obstacle.

A robot starts at the **top-left corner** of the grid and wants to reach the **bottom-right corner**.

The robot can move only:

- Right `→`
- Down `↓`

The robot cannot move through any cell containing an obstacle.

Return the number of possible unique paths to reach the bottom-right corner.

---

## Examples

### Example 1

**Input:**
```text
obstacleGrid = [
    [0,0,0],
    [0,1,0],
    [0,0,0]
]
```

**Output:**
```text
2
```

**Explanation:**

There are two possible paths:

```text
1. Right → Right → Down → Down
2. Down → Down → Right → Right
```

The middle cell contains an obstacle, so paths passing through that cell are not allowed.

---

### Example 2

**Input:**
```text
obstacleGrid = [
    [0,1],
    [0,0]
]
```

**Output:**
```text
1
```

**Explanation:**

The only possible path is:

```text
Down → Right
```

The cell `[0][1]` is an obstacle, so moving right first is not possible.

---

## Approach

We solve this problem using **Dynamic Programming**.

For each cell, the number of ways to reach it depends on the cells:

- Above it
- To its left

Normally:

```text
paths = top + left
```

However, if the current cell is an obstacle (`1`), the robot cannot enter that cell.

Therefore:

```text
if grid[i][j] == 1:
    paths = 0
```

For an empty cell:

```text
paths = top + left
```

We use a **1D DP array** to reduce the space required.

---

## Algorithm

1. Get the number of rows `m` and columns `n`.
2. Create a DP array of size `n` and initialize it with `0`.
3. Set `dp[0] = 1` because there is initially one way to reach the starting cell.
4. Traverse every cell of the grid.
5. If the current cell is an obstacle:
   ```text
   dp[j] = 0
   ```
6. Otherwise, if `j > 0`:
   ```text
   dp[j] = dp[j] + dp[j - 1]
   ```
7. After processing the entire grid, return `dp[n - 1]`.

---

## Dry Run

Consider:

```text
obstacleGrid = [
    [0,0,0],
    [0,1,0],
    [0,0,0]
]
```

Initially:

```text
dp = [1,0,0]
```

### First Row

After processing:

```text
dp = [1,1,1]
```

There is one way to reach each cell in the first row.

### Second Row

First cell:

```text
dp = [1,1,1]
```

Middle cell is an obstacle:

```text
dp[1] = 0
```

So:

```text
dp = [1,0,1]
```

The last cell receives paths only from above:

```text
dp = [1,0,1]
```

### Third Row

First cell:

```text
dp = [1,0,1]
```

Second cell:

```text
dp[1] = dp[1] + dp[0]
      = 0 + 1
      = 1
```

Now:

```text
dp = [1,1,1]
```

Third cell:

```text
dp[2] = dp[2] + dp[1]
      = 1 + 1
      = 2
```

Final:

```text
dp = [1,1,2]
```

Therefore:

```text
Answer = 2
```

---

## Solution

```python
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [0] * n
        dp[0] = 1

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                elif j > 0:
                    dp[j] += dp[j - 1]

        return dp[n - 1]
```

---

## How the Code Works

### Step 1: Get Grid Size

```python
m = len(obstacleGrid)
n = len(obstacleGrid[0])
```

`m` represents the number of rows and `n` represents the number of columns.

---

### Step 2: Create DP Array

```python
dp = [0] * n
dp[0] = 1
```

The DP array stores the number of ways to reach each column of the current row.

Initially, there is one way to reach the starting position.

---

### Step 3: Check Obstacles

```python
if obstacleGrid[i][j] == 1:
    dp[j] = 0
```

If a cell contains an obstacle, no path can pass through it.

Therefore, the number of ways to reach that cell becomes `0`.

---

### Step 4: Calculate Paths

```python
elif j > 0:
    dp[j] += dp[j - 1]
```

For an empty cell:

```text
Current cell = Top + Left
```

Here:

```text
dp[j]     → paths from above
dp[j - 1] → paths from left
```

---

## Important Edge Cases

### Starting Cell Is an Obstacle

If:

```text
obstacleGrid[0][0] = 1
```

there is no possible path.

The answer is:

```text
0
```

---

### Destination Is an Obstacle

If:

```text
obstacleGrid[m-1][n-1] = 1
```

the robot cannot reach the destination.

The answer is:

```text
0
```

---

### One Row

Example:

```text
[0,0,0,0]
```

There is only one possible path:

```text
→ → →
```

Answer:

```text
1
```

---

### One Column

Example:

```text
[
 [0],
 [0],
 [0]
]
```

There is only one possible path:

```text
↓
↓
```

Answer:

```text
1
```

---

## Complexity Analysis

Let:

- `m` = number of rows
- `n` = number of columns

### Time Complexity

```text
O(m × n)
```

We visit every cell exactly once.

### Space Complexity

```text
O(n)
```

We use only one 1D DP array.

---

## Key Concept

The main idea is:

```text
If cell is an obstacle:
    paths = 0

Otherwise:
    paths = paths from above + paths from left
```

In formula form:

```text
dp[i][j] = dp[i-1][j] + dp[i][j-1]
```

For an obstacle:

```text
dp[i][j] = 0
```

---

## Difference Between Unique Paths and Unique Paths II

| Feature | Unique Paths | Unique Paths II |
|---|---|---|
| Problem | LeetCode 62 | LeetCode 63 |
| Obstacles | No | Yes |
| Grid input | `m, n` | `obstacleGrid` |
| Movement | Right / Down | Right / Down |
| DP | Yes | Yes |
| Space | `O(n)` | `O(n)` |

---

## Constraints

- `1 <= m, n <= 100`
- `obstacleGrid[i][j]` is either `0` or `1`.
- The answer is guaranteed to be less than or equal to `2 * 10^9`.

---

## Language

**Python**

---

## LeetCode Information

- **Problem Number:** 63
- **Problem Name:** Unique Paths II
- **Difficulty:** Medium
- **Topic:** Dynamic Programming
- **Data Structure:** Array

---

## File Structure

```text
0063-unique-paths-ii/
│
├── README.md
└── solution.py
```

---

## Solution Link

[View Solution](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/0063-unique-paths-ii/solution.py)

---

## Repository Link

[LeetCode_solution](https://github.com/suchita4004-collab/LeetCode_solution)

---

## Main README Entry

Add this line to your main repository `README.md`:

```markdown
| 63 | [Unique Paths II](0063-unique-paths-ii/) | Medium |
```

After adding it, your sequence will continue:

```text
0062-unique-paths/
0063-unique-paths-ii/
```
