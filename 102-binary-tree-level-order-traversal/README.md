```markdown
# 102. Binary Tree Level Order Traversal

**Difficulty:** Medium  
**Language:** Python

---

## Problem

Given the root of a binary tree, return the level order traversal of its nodes' values.

Level order traversal means visiting the nodes:

- From left to right.
- Level by level.

For example:

```text
        3
       / \
      9   20
         /  \
        15   7
```

The level order traversal is:

```text
[[3], [9,20], [15,7]]
```

---

## Examples

### Example 1

**Input:**

```text
root = [3,9,20,null,null,15,7]
```

**Output:**

```text
[[3],[9,20],[15,7]]
```

**Explanation:**

The nodes are visited level by level:

```text
Level 1 → 3
Level 2 → 9, 20
Level 3 → 15, 7
```

---

### Example 2

**Input:**

```text
root = [1]
```

**Output:**

```text
[[1]]
```

**Explanation:**

There is only one node, so there is only one level.

---

### Example 3

**Input:**

```text
root = []
```

**Output:**

```text
[]
```

**Explanation:**

The tree is empty, so the result is also empty.

---

## Approach

We use **Breadth-First Search (BFS)** with a queue.

A queue follows **FIFO (First In, First Out)** order.

The basic idea is:

1. Put the root node into the queue.
2. Find how many nodes are present in the current level.
3. Remove those nodes one by one.
4. Store their values in the current level.
5. Add their left and right children to the queue.
6. Repeat until the queue becomes empty.

---

## Why Use a Queue?

Level order traversal needs to process nodes from top to bottom.

For example:

```text
        3
       / \
      9   20
         /  \
        15   7
```

The queue works like this:

```text
Start:
[3]

After processing 3:
[9, 20]

After processing 9 and 20:
[15, 7]

After processing 15 and 7:
[]
```

Therefore, the nodes are automatically processed level by level.

---

## Algorithm

```text
1. Create an empty result list.

2. If root is None:
       return []

3. Create a queue and add root.

4. While the queue is not empty:

       Find the number of nodes in the current level.

       Create an empty current_level list.

       Repeat for every node in the current level:

           Remove a node from the queue.
           Add its value to current_level.

           If left child exists:
               Add it to the queue.

           If right child exists:
               Add it to the queue.

       Add current_level to result.

5. Return result.
```

---

## Dry Run

Consider:

```text
        3
       / \
      9   20
         /  \
        15   7
```

### Step 1: Start

```text
Queue:
[3]

Result:
[]
```

Process `3`.

```text
Current level:
[3]

Queue:
[9, 20]
```

Add the current level:

```text
Result:
[[3]]
```

---

### Step 2: Process second level

Queue:

```text
[9, 20]
```

Process `9`:

```text
Current level:
[9]
```

Process `20`:

```text
Current level:
[9, 20]
```

Node `20` has two children, `15` and `7`.

So:

```text
Queue:
[15, 7]
```

Result:

```text
[[3], [9,20]]
```

---

### Step 3: Process third level

Queue:

```text
[15, 7]
```

Process both nodes:

```text
Current level:
[15, 7]
```

They have no children.

Queue becomes:

```text
[]
```

Final result:

```text
[[3], [9,20], [15,7]]
```

---

## How the Code Works

### 1. Import deque

```python
from collections import deque
```

`deque` provides an efficient queue for removing elements from the front.

---

### 2. Handle an empty tree

```python
if root is None:
    return result
```

If there is no root, there are no nodes to traverse.

---

### 3. Add root to queue

```python
queue = deque([root])
```

The traversal starts from the root.

---

### 4. Get current level size

```python
level_size = len(queue)
```

This is important because it tells us exactly how many nodes belong to the current level.

---

### 5. Process the current level

```python
for _ in range(level_size):
    node = queue.popleft()
    current_level.append(node.val)
```

Each node in the current level is removed and its value is stored.

---

### 6. Add children

```python
if node.left:
    queue.append(node.left)

if node.right:
    queue.append(node.right)
```

Children are added to the queue so they can be processed in the next level.

---

### 7. Store the level

```python
result.append(current_level)
```

After processing all nodes of the current level, we add that level to the final answer.

---

## Important Edge Cases

### 1. Empty tree

```text
root = []
```

Output:

```text
[]
```

---

### 2. Only one node

```text
    1
```

Output:

```text
[[1]]
```

---

### 3. Completely skewed tree

```text
1
 \
  2
   \
    3
     \
      4
```

Output:

```text
[[1],[2],[3],[4]]
```

Each node forms its own level.

---

### 4. Tree with missing children

```text
        1
       / \
      2   3
       \
        4
```

Output:

```text
[[1],[2,3],[4]]
```

The missing child is simply ignored.

---

## Complexity Analysis

Let `n` be the number of nodes in the tree.

### Time Complexity

```text
O(n)
```

Every node is visited exactly once.

### Space Complexity

```text
O(n)
```

The queue can contain up to `n` nodes in the worst case.

The result itself also contains all node values.

---

## Key Concept

The main concept is **Breadth-First Search (BFS)**.

```text
              Root
                ↓
           Level 1
                ↓
           Level 2
                ↓
           Level 3
                ↓
              ...
```

Using a queue:

```text
Front                         Rear
  ↓                             ↓
[Current nodes] → [Next nodes]
```

This allows us to process the tree from **top to bottom and left to right**.

---

## BFS vs DFS

| Feature | BFS | DFS |
|---|---|---|
| Used here | Yes | No |
| Main data structure | Queue | Stack / Recursion |
| Traversal | Level by level | Depth first |
| Suitable for level order | Yes | Less direct |
| Time | O(n) | O(n) |

---

## Constraints

- Number of nodes is in the range `[0, 2000]`.
- `-1000 <= Node.val <= 1000`.

---

## LeetCode Information

**Problem Number:** 102  
**Problem Name:** Binary Tree Level Order Traversal  
**Difficulty:** Medium  
**Topics:** Binary Tree, Breadth-First Search, Queue

---

## File Structure

```text
102-binary-tree-level-order-traversal/
│
├── README.md
└── solution.py
```

---

## Solution

[View solution.py](solution.py)

---

## Repository

[LeetCode Solution Repository](https://github.com/suchita4004-collab/LeetCode_solution)
```
