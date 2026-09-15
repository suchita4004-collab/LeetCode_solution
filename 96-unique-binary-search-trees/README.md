```markdown
# 96. Unique Binary Search Trees

**Difficulty:** Medium  
**Language:** Python

## Problem

Given an integer `n`, return the number of structurally unique Binary Search Trees (BSTs) that can be formed using exactly `n` nodes.

The nodes contain unique values from:

```text
1 to n
```

We only need to return the **number of different BST structures**, not the actual trees.

---

## Examples

### Example 1

**Input:**

```text
n = 3
```

**Output:**

```text
5
```

There are 5 structurally unique BSTs that can be created using 3 nodes.

---

### Example 2

**Input:**

```text
n = 1
```

**Output:**

```text
1
```

Only one BST is possible:

```text
1
```

---

## Approach

I use **Dynamic Programming** to solve this problem.

Let:

```text
dp[i]
```

represent the number of unique BSTs that can be formed using `i` nodes.

For every possible root, the nodes smaller than the root form the left subtree and the nodes greater than the root form the right subtree.

If we have `nodes` total nodes and choose `root` as the root:

```text
Left nodes  = root - 1
Right nodes = nodes - root
```

The number of trees for this root is:

```text
dp[left_nodes] × dp[right_nodes]
```

We calculate this for every possible root and add all the results.

---

## Algorithm

1. Create a DP array of size `n + 1`.
2. Set:

```text
dp[0] = 1
```

There is one way to form an empty tree.

3. For every number of nodes from `1` to `n`:
   - Try every possible node as the root.
   - Calculate the number of nodes in the left subtree.
   - Calculate the number of nodes in the right subtree.
   - Multiply the number of possible left and right subtrees.
   - Add the result to `dp[nodes]`.
4. Return `dp[n]`.

---

## Code

```python
class Solution:
    def numTrees(self, n):
        dp = [0] * (n + 1)

        dp[0] = 1

        for nodes in range(1, n + 1):
            for root in range(1, nodes + 1):
                left_nodes = root - 1
                right_nodes = nodes - root

                dp[nodes] += dp[left_nodes] * dp[right_nodes]

        return dp[n]
```

---

## Dry Run

Let's take:

```text
n = 3
```

We create:

```text
dp = [1, 0, 0, 0]
```

Here:

```text
dp[0] = 1
```

### For 1 node

Only `1` can be the root.

```text
Left = 0
Right = 0
```

So:

```text
dp[1] = dp[0] × dp[0]
      = 1 × 1
      = 1
```

Now:

```text
dp = [1, 1, 0, 0]
```

---

### For 2 nodes

There are two possible roots.

#### Root = 1

```text
Left = 0
Right = 1
```

Number of trees:

```text
dp[0] × dp[1]
= 1 × 1
= 1
```

#### Root = 2

```text
Left = 1
Right = 0
```

Number of trees:

```text
dp[1] × dp[0]
= 1 × 1
= 1
```

Therefore:

```text
dp[2] = 2
```

Now:

```text
dp = [1, 1, 2, 0]
```

---

### For 3 nodes

There are three possible roots.

#### Root = 1

```text
Left = 0
Right = 2

dp[0] × dp[2]
= 1 × 2
= 2
```

#### Root = 2

```text
Left = 1
Right = 1

dp[1] × dp[1]
= 1 × 1
= 1
```

#### Root = 3

```text
Left = 2
Right = 0

dp[2] × dp[0]
= 2 × 1
= 2
```

Therefore:

```text
dp[3] = 2 + 1 + 2
      = 5
```

Final answer:

```text
5
```

---

## How Code Works

### 1. Create DP Array

```python
dp = [0] * (n + 1)
```

This stores the number of unique BSTs for every number of nodes.

For `n = 3`:

```text
dp = [0, 0, 0, 0]
```

---

### 2. Empty Tree

```python
dp[0] = 1
```

An empty tree is considered one possible subtree.

This is important when the root has no left or right child.

---

### 3. Select Every Possible Root

```python
for root in range(1, nodes + 1):
```

Every node can become the root.

For example, with 3 nodes:

```text
Root = 1
Root = 2
Root = 3
```

---

### 4. Calculate Left and Right Nodes

```python
left_nodes = root - 1
right_nodes = nodes - root
```

For example, if:

```text
nodes = 5
root = 3
```

then:

```text
Left nodes  = 2
Right nodes = 2
```

The structure is:

```text
        3
       / \
      2   2
    nodes nodes
```

---

### 5. Multiply Possibilities

```python
dp[nodes] += dp[left_nodes] * dp[right_nodes]
```

Every possible left subtree can be combined with every possible right subtree.

Therefore, we multiply their counts.

---

## Catalan Numbers

The number of unique BSTs follows the **Catalan number** sequence.

For example:

```text
n = 0  → 1
n = 1  → 1
n = 2  → 2
n = 3  → 5
n = 4  → 14
n = 5  → 42
n = 6  → 132
n = 7  → 429
n = 8  → 1430
```

For this problem, `n` can be as large as `19`.

The answer for `n = 19` is:

```text
1767263190
```

---

## Important Edge Cases

### 1. `n = 1`

```text
Input: 1
Output: 1
```

Only one BST is possible.

### 2. `n = 2`

```text
Input: 2
Output: 2
```

The two structures are:

```text
1          2
 \        /
  2      1
```

### 3. `n = 3`

```text
Input: 3
Output: 5
```

There are 5 different BST structures.

---

## Difference Between #95 and #96

### #95 – Unique Binary Search Trees II

Returns the **actual BSTs**.

```text
n = 3

Output = 5 different trees
```

### #96 – Unique Binary Search Trees

Returns only the **number of BSTs**.

```text
n = 3

Output = 5
```

So #96 is simpler because we don't need to construct and store the trees.

---

## Complexity Analysis

There are two nested loops.

**Time Complexity:** `O(n²)`

For every number of nodes, we try every possible root.

**Space Complexity:** `O(n)`

We only store the DP array.

---

## Key Concept

The main concept used in this problem is **Dynamic Programming**.

The important idea is:

```text
Number of BSTs
      ↓
Choose root
      ↓
Left subtree × Right subtree
      ↓
Add for every possible root
```

Formula:

```text
dp[nodes] += dp[left_nodes] × dp[right_nodes]
```

This is also related to the **Catalan Number** sequence.

---

## Constraints

- `1 <= n <= 19`
- Nodes have unique values from `1` to `n`.

---

## LeetCode Information

**Problem Number:** 96  
**Problem Name:** Unique Binary Search Trees  
**Difficulty:** Medium  
**Topic:** Dynamic Programming, Binary Search Tree, Catalan Numbers

---

## File Structure

```text
96-unique-binary-search-trees/
│
├── README.md
└── solution.py
```

---

## Solution

[View solution.py](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/96-unique-binary-search-trees/solution.py)

---

## Repository

[LeetCode_solution](https://github.com/suchita4004-collab/LeetCode_solution)
```
