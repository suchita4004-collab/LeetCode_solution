```markdown
# 103. Binary Tree Zigzag Level Order Traversal

**Difficulty:** Medium  
**Language:** Python

---

## Problem

Given the root of a binary tree, return the zigzag level order traversal of its nodes' values.

In normal level order traversal, nodes are visited from left to right at every level.

In zigzag level order traversal, the direction changes at every level:

```text
Level 1 → Left to Right
Level 2 → Right to Left
Level 3 → Left to Right
Level 4 → Right to Left
...
```

For example:

```text
        3
       / \
      9   20
         /  \
        15   7
```

The zigzag traversal is:

```text
[[3], [20,9], [15,7]]
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
[[3],[20,9],[15,7]]
```

**Explanation:**

The traversal is:

```text
Level 1 → 3
Level 2 → 20, 9
Level 3 → 15, 7
```

The direction changes at every level.

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

There is only one level, so no direction change is needed.

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

The tree is empty.

---

## Approach

We use **Breadth-First Search (BFS)** with a queue.

The main difference from normal level order traversal is that we reverse every alternate level.

We use a Boolean variable:

```python
left_to_right = True
```

It tells us the direction of the current level.

### Direction

```text
True  → Left to Right
False → Right to Left
```

After processing each level, we change the direction.

---

## Algorithm

```text
1. If root is None:
       return []

2. Create a queue and add root.

3. Set left_to_right = True.

4. While the queue is not empty:

       Find the number of nodes in the current level.

       Create an empty current_level list.

       Process all nodes of the current level.

       Add their children to the queue.

       If direction is Right to Left:
           reverse current_level.

       Add current_level to result.

       Change the direction.

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

### Level 1

Direction:

```text
Left → Right
```

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

Change direction.

---

### Level 2

Direction:

```text
Right → Left
```

Queue:

```text
[9, 20]
```

Normal order:

```text
[9, 20]
```

Since the direction is right to left, reverse it:

```text
[20, 9]
```

Result:

```text
[[3], [20,9]]
```

Change direction.

---

### Level 3

Direction:

```text
Left → Right
```

Queue:

```text
[15, 7]
```

Current level:

```text
[15, 7]
```

No reversal is required.

Final result:

```text
[[3], [20,9], [15,7]]
```

---

## How the Code Works

### 1. Handle empty tree

```python
if root is None:
    return result
```

If there are no nodes, return an empty list.

---

### 2. Create the queue

```python
queue = deque([root])
```

The queue is used for BFS traversal.

---

### 3. Store the direction

```python
left_to_right = True
```

Initially, we process the first level from left to right.

---

### 4. Process one level

```python
level_size = len(queue)
current_level = []

for _ in range(level_size):
    node = queue.popleft()
    current_level.append(node.val)
```

`level_size` tells us how many nodes belong to the current level.

---

### 5. Add children

```python
if node.left:
    queue.append(node.left)

if node.right:
    queue.append(node.right)
```

The children will be processed in the next level.

---

### 6. Reverse alternate levels

```python
if not left_to_right:
    current_level.reverse()
```

When the direction is right to left, we reverse the values collected from the queue.

---

### 7. Change direction

```python
left_to_right = not left_to_right
```

This changes:

```text
True → False
False → True
```

So the direction alternates at every level.

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

### 2. Single node

```text
    1
```

Output:

```text
[[1]]
```

---

### 3. Two levels

```text
        1
       / \
      2   3
```

Output:

```text
[[1], [3,2]]
```

The second level is reversed.

---

### 4. Skewed tree

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
[[1], [2], [3], [4]]
```

Each level contains only one node, so reversing does not change the result.

---

## Normal Level Order vs Zigzag

For the same tree:

```text
        3
       / \
      9   20
         /  \
        15   7
```

### Normal Level Order

```text
[[3], [9,20], [15,7]]
```

### Zigzag Level Order

```text
[[3], [20,9], [15,7]]
```

The second level is reversed.

---

## Complexity Analysis

Let `n` be the number of nodes in the tree.

### Time Complexity

```text
O(n)
```

Every node is visited exactly once.

Reversing each level takes time proportional to the number of nodes in that level. Across all levels, this is still `O(n)`.

### Space Complexity

```text
O(n)
```

The queue can contain many nodes at the same time, and the result also stores all node values.

---

## Key Concept

The main idea is:

```text
          Binary Tree
               ↓
              BFS
               ↓
        Process level by level
               ↓
      ┌────────┴────────┐
      ↓                 ↓
Left → Right       Right → Left
      ↓                 ↓
      └───────┬─────────┘
              ↓
        Repeat alternately
```

The important line is:

```python
if not left_to_right:
    current_level.reverse()
```

This converts normal level order traversal into zigzag traversal.

---

## Constraints

- Number of nodes is in the range `[0, 2000]`.
- `-100 <= Node.val <= 100`.

---

## LeetCode Information

**Problem Number:** 103  
**Problem Name:** Binary Tree Zigzag Level Order Traversal  
**Difficulty:** Medium  
**Topics:** Binary Tree, Breadth-First Search, Queue

---

## File Structure

```text
103-binary-tree-zigzag-level-order-traversal/
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
