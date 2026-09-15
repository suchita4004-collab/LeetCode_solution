```markdown
# 100. Same Tree

**Difficulty:** Easy  
**Language:** Python

---

## Problem

Given the roots of two binary trees `p` and `q`, check whether they are the same or not.

Two binary trees are considered the same when:

1. They have the same structure.
2. Corresponding nodes have the same values.

If both conditions are satisfied, return `True`. Otherwise, return `False`.

---

## Examples

### Example 1

**Input:**

```text
p = [1,2,3]
q = [1,2,3]
```

**Output:**

```text
true
```

**Explanation:**

Both trees have the same structure and the corresponding nodes contain the same values.

---

### Example 2

**Input:**

```text
p = [1,2]
q = [1,null,2]
```

**Output:**

```text
false
```

**Explanation:**

The values are similar, but the structure is different.

In the first tree, `2` is the left child.

In the second tree, `2` is the right child.

Therefore, the trees are not the same.

---

### Example 3

**Input:**

```text
p = [1,2,1]
q = [1,1,2]
```

**Output:**

```text
false
```

**Explanation:**

The tree structures are the same, but the corresponding node values are different.

Therefore, the trees are not the same.

---

## Approach

We compare both trees recursively.

For every pair of corresponding nodes:

1. If both nodes are `None`, they are the same.
2. If only one node is `None`, the trees are different.
3. If their values are different, the trees are different.
4. Otherwise, compare their left subtrees.
5. Compare their right subtrees.

The trees are the same only when all corresponding nodes match.

---

## Algorithm

```text
isSameTree(p, q)

1. If p and q are both None:
       return True

2. If p is None or q is None:
       return False

3. If p.val != q.val:
       return False

4. Check the left subtrees.

5. Check the right subtrees.

6. Return True if both subtrees are the same.
```

---

## Dry Run

Consider:

```text
Tree p:          Tree q:

    1                1
   / \              / \
  2   3            2   3
```

### Step 1

Compare root values:

```text
1 == 1
```

So, continue.

### Step 2

Compare left children:

```text
2 == 2
```

Continue.

### Step 3

Compare right children:

```text
3 == 3
```

Continue.

### Step 4

Both remaining children are `None`.

Therefore:

```text
True
```

The two trees are the same.

---

## Example of Different Structure

```text
Tree p:          Tree q:

    1                1
   /                  \
  2                    2
```

Root values are equal:

```text
1 == 1
```

But:

```text
p.left  = 2
q.left  = None
```

One node exists while the other does not.

Therefore:

```text
False
```

---

## How the Code Works

### 1. Check if both nodes are empty

```python
if p is None and q is None:
    return True
```

If both nodes are empty at the same position, there is no difference.

### 2. Check if only one node is empty

```python
if p is None or q is None:
    return False
```

This means the tree structures are different.

### 3. Compare node values

```python
if p.val != q.val:
    return False
```

If the values are different, the trees cannot be the same.

### 4. Compare both subtrees

```python
return (
    self.isSameTree(p.left, q.left)
    and self.isSameTree(p.right, q.right)
)
```

The left and right subtrees must both be identical.

---

## Important Edge Cases

### 1. Both trees are empty

```text
p = []
q = []
```

Output:

```text
True
```

### 2. One tree is empty

```text
p = []
q = [1]
```

Output:

```text
False
```

### 3. Same structure but different values

```text
p = [1,2,3]
q = [1,2,4]
```

Output:

```text
False
```

### 4. Same values but different structure

```text
p = [1,2]
q = [1,null,2]
```

Output:

```text
False
```

---

## Complexity Analysis

Let `n` be the number of nodes that are compared.

### Time Complexity

```text
O(n)
```

Each corresponding node is checked at most once.

### Space Complexity

```text
O(h)
```

The recursive calls use the height of the tree.

For a balanced tree:

```text
O(log n)
```

For a skewed tree:

```text
O(n)
```

---

## Key Concept

The main idea is:

```text
Compare two nodes
       ↓
Are both None?
       ↓
     Yes → Same
       ↓
Are only one None?
       ↓
     Yes → Different
       ↓
Compare values
       ↓
Compare left subtrees
       ↓
Compare right subtrees
       ↓
Both match → Same Tree
```

---

## Constraints

- Number of nodes in both trees is in the range `[0, 100]`.
- `-10^4 <= Node.val <= 10^4`

---

## LeetCode Information

**Problem Number:** 100  
**Problem Name:** Same Tree  
**Difficulty:** Easy  
**Topics:** Binary Tree, Depth-First Search, Recursion

---

## File Structure

```text
100-same-tree/
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
