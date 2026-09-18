# 107. Binary Tree Level Order Traversal II

**Difficulty:** Medium  
**Language:** Python

## Problem

Given the `root` of a binary tree, return the **bottom-up level order traversal** of its nodes' values.

This means:

- Traverse the tree level by level.
- Start from the root level.
- Store each level from left to right.
- Finally, return the levels in **reverse order**, from the leaf level to the root.

## Examples

### Example 1

**Input:**
```text
root = [3,9,20,null,null,15,7]
```

**Tree:**

```text
        3
       / \
      9   20
         /  \
        15   7
```

Normal level order:

```text
[[3], [9,20], [15,7]]
```

Bottom-up level order:

```text
[[15,7], [9,20], [3]]
```

**Output:**
```text
[[15,7],[9,20],[3]]
```

### Example 2

**Input:**
```text
root = [1]
```

**Output:**
```text
[[1]]
```

### Example 3

**Input:**
```text
root = []
```

**Output:**
```text
[]
```

## Approach

We can use **Breadth-First Search (BFS)** to traverse the tree level by level.

The normal level order traversal gives:

```text
Root → Children → Grandchildren → ...
```

But we need:

```text
Leaves → Parent levels → Root
```

So we can:

1. Use a queue to perform normal level order traversal.
2. Store the values of each level in a list.
3. Reverse the final list before returning it.

## Algorithm

```text
1. Create an empty result list.
2. If root is None, return [].
3. Create a queue and insert the root.
4. While the queue is not empty:
   a. Find the number of nodes in the current level.
   b. Create an empty list for the current level.
   c. Remove each node of the current level.
   d. Add its value to the current level.
   e. Add its left and right children to the queue.
   f. Add the current level to result.
5. Reverse result.
6. Return result.
```

## Dry Run

For:

```text
root = [3,9,20,null,null,15,7]
```

Tree:

```text
        3
       / \
      9   20
         /  \
        15   7
```

### Level 1

Queue:

```text
[3]
```

Current level:

```text
[3]
```

Result:

```text
[[3]]
```

### Level 2

Queue:

```text
[9,20]
```

Current level:

```text
[9,20]
```

Result:

```text
[[3],[9,20]]
```

### Level 3

Queue:

```text
[15,7]
```

Current level:

```text
[15,7]
```

Result:

```text
[[3],[9,20],[15,7]]
```

Now reverse the result:

```text
[[15,7],[9,20],[3]]
```

Therefore, the final answer is:

```text
[[15,7],[9,20],[3]]
```

## How the Code Works

A `deque` is used as a queue because removing an element from the beginning is efficient.

```python
queue = deque([root])
```

We process one complete level at a time:

```python
level_size = len(queue)
```

For every node in that level:

```python
node = queue.popleft()
current_level.append(node.val)
```

Then we add its children:

```python
if node.left:
    queue.append(node.left)

if node.right:
    queue.append(node.right)
```

After processing all levels, we reverse the result:

```python
result.reverse()
```

This changes:

```text
[[3], [9,20], [15,7]]
```

into:

```text
[[15,7], [9,20], [3]]
```

## Important Edge Cases

### 1. Empty tree

```text
root = []
```

There are no nodes, so the answer is:

```text
[]
```

### 2. Single node

```text
root = [1]
```

The answer is:

```text
[[1]]
```

### 3. Skewed tree

If the tree contains only left or right children, each level will contain one node. Reversing the levels still gives the correct bottom-up traversal.

## Complexity Analysis

Let `n` be the number of nodes.

### Time Complexity

```text
O(n)
```

Every node is visited exactly once. Reversing the level list takes at most `O(n)` as well.

### Space Complexity

```text
O(n)
```

The queue and result list can both contain information proportional to the number of nodes.

## Key Concept

The main concept is **Breadth-First Search (BFS)**.

Normal level order:

```text
Root
 ↓
Children
 ↓
Grandchildren
```

Bottom-up level order:

```text
Grandchildren
 ↓
Children
 ↓
Root
```

So, we perform normal BFS and then reverse the list of levels.

## Constraints

- Number of nodes is in the range `[0, 2000]`.
- `-1000 <= Node.val <= 1000`.

## LeetCode Information

- **Problem:** Binary Tree Level Order Traversal II
- **Problem Number:** 107
- **Difficulty:** Medium
- **Language:** Python

## File Structure

```text
107-binary-tree-level-order-traversal-ii/
│
├── README.md
└── solution.py
```

## Solution

See [`solution.py`](solution.py) for the complete Python solution.

## Repository

**GitHub Repository:** `LeetCode_solution`
