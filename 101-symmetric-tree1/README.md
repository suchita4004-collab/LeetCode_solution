```markdown
# 101. Symmetric Tree

**Difficulty:** Easy  
**Language:** Python

---

## Problem

Given the root of a binary tree, check whether the tree is a mirror of itself.

A binary tree is symmetric if its left and right sides are mirror images of each other.

For example:

```text
        1
       / \
      2   2
     / \ / \
    3  4 4  3
```

This tree is symmetric because the left side and right side are mirror images.

---

## Examples

### Example 1

**Input:**

```text
root = [1,2,2,3,4,4,3]
```

**Output:**

```text
true
```

**Explanation:**

The left and right subtrees are mirror images of each other.

---

### Example 2

**Input:**

```text
root = [1,2,2,null,3,null,3]
```

**Output:**

```text
false
```

**Explanation:**

The left and right subtrees do not have the same structure, so the tree is not symmetric.

---

# Approach 1: Recursive

The recursive approach checks two nodes at a time.

Two nodes are mirror images when:

1. Both nodes are `None`.
2. Only one node is `None` → not a mirror.
3. Their values are equal.
4. The left child of the first node matches the right child of the second node.
5. The right child of the first node matches the left child of the second node.

---

## Recursive Algorithm

```text
isMirror(left, right)

1. If both are None:
       return True

2. If only one is None:
       return False

3. If values are different:
       return False

4. Compare:
       left.left  with right.right
       left.right with right.left

5. Return True if both comparisons are True.
```

---

## Recursive Code

```python
def isSymmetricRecursive(self, root):
    def isMirror(left, right):
        if left is None and right is None:
            return True

        if left is None or right is None:
            return False

        if left.val != right.val:
            return False

        return (
            isMirror(left.left, right.right)
            and isMirror(left.right, right.left)
        )

    if root is None:
        return True

    return isMirror(root.left, root.right)
```

---

## Recursive Dry Run

Consider:

```text
        1
       / \
      2   2
     / \ / \
    3  4 4  3
```

Start with:

```text
left = 2
right = 2
```

Values are equal.

Now compare opposite children:

```text
left.left  = 3    ↔    right.right = 3
left.right = 4    ↔    right.left  = 4
```

Both pairs match.

Therefore:

```text
True
```

The tree is symmetric.

---

# Approach 2: Iterative

The iterative approach uses a **queue**.

Instead of using recursion, we store pairs of nodes that should be mirrors of each other.

For every pair:

```text
(left, right)
```

we check:

```text
left.val == right.val
```

Then add their opposite children to the queue.

---

## Iterative Algorithm

```text
1. Create a queue containing:
       (root.left, root.right)

2. While the queue is not empty:

       Remove a pair of nodes.

       If both are None:
           continue

       If only one is None:
           return False

       If values are different:
           return False

       Add:
           (left.left, right.right)
           (left.right, right.left)

3. If all pairs match:
       return True
```

---

## Iterative Dry Run

For:

```text
        1
       / \
      2   2
     / \ / \
    3  4 4  3
```

Initially:

```text
Queue:
(2, 2)
```

Compare:

```text
2 == 2
```

Add opposite pairs:

```text
(3, 3)
(4, 4)
```

Compare:

```text
3 == 3
4 == 4
```

All remaining pairs are `None`.

Therefore:

```text
True
```

---

## How the Code Works

### Check both nodes

```python
if left is None and right is None:
    continue
```

If both nodes are empty, that part is symmetric.

### Check only one node

```python
if left is None or right is None:
    return False
```

This means the structure is different.

### Compare values

```python
if left.val != right.val:
    return False
```

Mirror nodes must have the same value.

### Add opposite children

```python
queue.append((left.left, right.right))
queue.append((left.right, right.left))
```

This is the main idea of the problem.

We compare:

```text
Left side              Right side

left.left      ↔       right.right
left.right     ↔       right.left
```

---

## Important Edge Cases

### 1. Single node

```text
root = [1]
```

Output:

```text
True
```

A single node is symmetric.

### 2. Two equal children

```text
    1
   / \
  2   2
```

Output:

```text
True
```

### 3. Different values

```text
    1
   / \
  2   3
```

Output:

```text
False
```

### 4. Same values but different structure

```text
    1
   / \
  2   2
   \   \
    3   3
```

Output:

```text
False
```

The structure is not a mirror.

---

## Recursive vs Iterative

| Feature | Recursive | Iterative |
|---|---|---|
| Technique | Recursion | Queue |
| Data structure | Call stack | Queue |
| Time | O(n) | O(n) |
| Space | O(h) | O(n) |
| Easy to understand | Yes | Yes |
| Avoids recursion | No | Yes |

Where `h` is the height of the tree.

---

## Complexity Analysis

### Recursive

**Time Complexity:**

```text
O(n)
```

Every node is visited at most once.

**Space Complexity:**

```text
O(h)
```

The recursion stack depends on the height of the tree.

---

### Iterative

**Time Complexity:**

```text
O(n)
```

Every node is processed at most once.

**Space Complexity:**

```text
O(n)
```

The queue can contain multiple nodes.

---

## Key Concept

The main idea is:

```text
          Root
         /    \
        L      R
       / \    / \
      A   B  C   D

Compare:

L.value == R.value

L.left  ↔ R.right
L.right ↔ R.left
```

So, for a symmetric tree:

```text
Left subtree = Mirror image of Right subtree
```

---

## Constraints

- Number of nodes is in the range `[1, 1000]`.
- `-100 <= Node.val <= 100`.
- The tree can contain duplicate values.

---

## Follow Up

The problem asks for both recursive and iterative solutions.

This solution provides:

1. **Recursive solution** using `isMirror()`.
2. **Iterative solution** using a queue.

The iterative solution is used as the main LeetCode method:

```python
def isSymmetric(self, root):
```

---

## LeetCode Information

**Problem Number:** 101  
**Problem Name:** Symmetric Tree  
**Difficulty:** Easy  
**Topics:** Binary Tree, Depth-First Search, Breadth-First Search, Recursion, Queue

---

## File Structure

```text
101-symmetric-tree/
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
``````markdown
# 101. Symmetric Tree

**Difficulty:** Easy  
**Language:** Python

---

## Problem

Given the root of a binary tree, check whether the tree is a mirror of itself.

A binary tree is symmetric if its left and right sides are mirror images of each other.

For example:

```text
        1
       / \
      2   2
     / \ / \
    3  4 4  3
```

This tree is symmetric because the left side and right side are mirror images.

---

## Examples

### Example 1

**Input:**

```text
root = [1,2,2,3,4,4,3]
```

**Output:**

```text
true
```

**Explanation:**

The left and right subtrees are mirror images of each other.

---

### Example 2

**Input:**

```text
root = [1,2,2,null,3,null,3]
```

**Output:**

```text
false
```

**Explanation:**

The left and right subtrees do not have the same structure, so the tree is not symmetric.

---

# Approach 1: Recursive

The recursive approach checks two nodes at a time.

Two nodes are mirror images when:

1. Both nodes are `None`.
2. Only one node is `None` → not a mirror.
3. Their values are equal.
4. The left child of the first node matches the right child of the second node.
5. The right child of the first node matches the left child of the second node.

---

## Recursive Algorithm

```text
isMirror(left, right)

1. If both are None:
       return True

2. If only one is None:
       return False

3. If values are different:
       return False

4. Compare:
       left.left  with right.right
       left.right with right.left

5. Return True if both comparisons are True.
```

---

## Recursive Code

```python
def isSymmetricRecursive(self, root):
    def isMirror(left, right):
        if left is None and right is None:
            return True

        if left is None or right is None:
            return False

        if left.val != right.val:
            return False

        return (
            isMirror(left.left, right.right)
            and isMirror(left.right, right.left)
        )

    if root is None:
        return True

    return isMirror(root.left, root.right)
```

---

## Recursive Dry Run

Consider:

```text
        1
       / \
      2   2
     / \ / \
    3  4 4  3
```

Start with:

```text
left = 2
right = 2
```

Values are equal.

Now compare opposite children:

```text
left.left  = 3    ↔    right.right = 3
left.right = 4    ↔    right.left  = 4
```

Both pairs match.

Therefore:

```text
True
```

The tree is symmetric.

---

# Approach 2: Iterative

The iterative approach uses a **queue**.

Instead of using recursion, we store pairs of nodes that should be mirrors of each other.

For every pair:

```text
(left, right)
```

we check:

```text
left.val == right.val
```

Then add their opposite children to the queue.

---

## Iterative Algorithm

```text
1. Create a queue containing:
       (root.left, root.right)

2. While the queue is not empty:

       Remove a pair of nodes.

       If both are None:
           continue

       If only one is None:
           return False

       If values are different:
           return False

       Add:
           (left.left, right.right)
           (left.right, right.left)

3. If all pairs match:
       return True
```

---

## Iterative Dry Run

For:

```text
        1
       / \
      2   2
     / \ / \
    3  4 4  3
```

Initially:

```text
Queue:
(2, 2)
```

Compare:

```text
2 == 2
```

Add opposite pairs:

```text
(3, 3)
(4, 4)
```

Compare:

```text
3 == 3
4 == 4
```

All remaining pairs are `None`.

Therefore:

```text
True
```

---

## How the Code Works

### Check both nodes

```python
if left is None and right is None:
    continue
```

If both nodes are empty, that part is symmetric.

### Check only one node

```python
if left is None or right is None:
    return False
```

This means the structure is different.

### Compare values

```python
if left.val != right.val:
    return False
```

Mirror nodes must have the same value.

### Add opposite children

```python
queue.append((left.left, right.right))
queue.append((left.right, right.left))
```

This is the main idea of the problem.

We compare:

```text
Left side              Right side

left.left      ↔       right.right
left.right     ↔       right.left
```

---

## Important Edge Cases

### 1. Single node

```text
root = [1]
```

Output:

```text
True
```

A single node is symmetric.

### 2. Two equal children

```text
    1
   / \
  2   2
```

Output:

```text
True
```

### 3. Different values

```text
    1
   / \
  2   3
```

Output:

```text
False
```

### 4. Same values but different structure

```text
    1
   / \
  2   2
   \   \
    3   3
```

Output:

```text
False
```

The structure is not a mirror.

---

## Recursive vs Iterative

| Feature | Recursive | Iterative |
|---|---|---|
| Technique | Recursion | Queue |
| Data structure | Call stack | Queue |
| Time | O(n) | O(n) |
| Space | O(h) | O(n) |
| Easy to understand | Yes | Yes |
| Avoids recursion | No | Yes |

Where `h` is the height of the tree.

---

## Complexity Analysis

### Recursive

**Time Complexity:**

```text
O(n)
```

Every node is visited at most once.

**Space Complexity:**

```text
O(h)
```

The recursion stack depends on the height of the tree.

---

### Iterative

**Time Complexity:**

```text
O(n)
```

Every node is processed at most once.

**Space Complexity:**

```text
O(n)
```

The queue can contain multiple nodes.

---

## Key Concept

The main idea is:

```text
          Root
         /    \
        L      R
       / \    / \
      A   B  C   D

Compare:

L.value == R.value

L.left  ↔ R.right
L.right ↔ R.left
```

So, for a symmetric tree:

```text
Left subtree = Mirror image of Right subtree
```

---

## Constraints

- Number of nodes is in the range `[1, 1000]`.
- `-100 <= Node.val <= 100`.
- The tree can contain duplicate values.

---

## Follow Up

The problem asks for both recursive and iterative solutions.

This solution provides:

1. **Recursive solution** using `isMirror()`.
2. **Iterative solution** using a queue.

The iterative solution is used as the main LeetCode method:

```python
def isSymmetric(self, root):
```

---

## LeetCode Information

**Problem Number:** 101  
**Problem Name:** Symmetric Tree  
**Difficulty:** Easy  
**Topics:** Binary Tree, Depth-First Search, Breadth-First Search, Recursion, Queue

---

## File Structure

```text
101-symmetric-tree/
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
