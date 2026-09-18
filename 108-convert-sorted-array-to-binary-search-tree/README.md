# 108. Convert Sorted Array to Binary Search Tree

**Difficulty:** Easy  
**Language:** Python

## Problem

Given an integer array `nums` sorted in **ascending order**, convert it into a **height-balanced Binary Search Tree (BST)**.

A height-balanced binary tree is a tree where the heights of the left and right subtrees of every node differ by at most 1.

## Examples

### Example 1

**Input:**
```text
nums = [-10,-3,0,5,9]
```

**Output:**
```text
[0,-3,9,-10,null,5]
```

The tree is:

```text
        0
       / \
     -3   9
     /   /
   -10   5
```

Another valid answer is:

```text
[0,-10,5,null,-3,null,9]
```

Both trees are height-balanced BSTs.

### Example 2

**Input:**
```text
nums = [1,3]
```

**Output:**
```text
[3,1]
```

Another valid answer is:

```text
[1,null,3]
```

Both are height-balanced BSTs.

## Approach

Since the array is already sorted, the **middle element** is the best choice for the root.

For example:

```text
[-10, -3, 0, 5, 9]
          ↑
        middle
```

`0` becomes the root.

Then:

- Elements before `0` form the left subtree.
- Elements after `0` form the right subtree.
- We repeat the same process recursively.

This keeps both sides approximately equal in size.

genui{"learning_viz":{"type_id":"BINARY_SEARCH_TREE_INSERTION","initial_values":{"insertionSequence":"balanced"}}}

## Algorithm

```text
1. If the current range is empty, return None.
2. Find the middle element of the current range.
3. Create a TreeNode using the middle element.
4. Recursively build the left subtree using elements before the middle.
5. Recursively build the right subtree using elements after the middle.
6. Return the root.
```

## Dry Run

For:

```text
nums = [-10,-3,0,5,9]
```

### Step 1

Middle element is `0`.

```text
        0
       / \
```

Left part:

```text
[-10,-3]
```

Right part:

```text
[5,9]
```

### Step 2

For `[-10,-3]`, choose `-3` as the middle:

```text
        0
       /
     -3
     /
   -10
```

### Step 3

For `[5,9]`, choose `9` as the middle:

```text
        0
       / \
     -3   9
     /   /
   -10   5
```

Therefore, the resulting tree can be represented as:

```text
[0,-3,9,-10,null,5]
```

## How the Code Works

We use two pointers, `left` and `right`, to represent the current portion of the array.

The middle index is calculated as:

```python
mid = (left + right) // 2
```

The middle value becomes the root:

```python
root = TreeNode(nums[mid])
```

Then we recursively construct both sides:

```python
root.left = build(left, mid - 1)
root.right = build(mid + 1, right)
```

This process continues until:

```python
left > right
```

At that point, there are no elements left, so we return `None`.

## Important Edge Cases

### 1. One element

```text
nums = [1]
```

The only element becomes the root.

Output:

```text
[1]
```

### 2. Two elements

```text
nums = [1,3]
```

Either element can be selected as the root as long as the resulting tree is height-balanced.

### 3. Large array

The recursive solution works efficiently even when the array contains up to `10^4` elements.

## Complexity Analysis

Let `n` be the number of elements in `nums`.

### Time Complexity

```text
O(n)
```

Every element is used exactly once to create a tree node.

### Space Complexity

```text
O(log n)
```

The recursion depth is `O(log n)` because the tree is height-balanced.

The tree itself contains `O(n)` nodes, but the **extra auxiliary recursion space** is `O(log n)`.

## Key Concept

The main idea is:

```text
Sorted Array
     ↓
Choose Middle Element
     ↓
     Root
    /    \
 Left    Right
  ↓        ↓
Repeat   Repeat
```

Choosing the middle element ensures that the number of elements on both sides is nearly equal, which produces a height-balanced BST.

## Constraints

- `1 <= nums.length <= 10^4`
- `-10^4 <= nums[i] <= 10^4`
- `nums` is sorted in strictly increasing order.

## LeetCode Information

- **Problem:** Convert Sorted Array to Binary Search Tree
- **Problem Number:** 108
- **Difficulty:** Easy
- **Language:** Python

## File Structure

```text
108-convert-sorted-array-to-binary-search-tree/
│
├── README.md
└── solution.py
```

## Solution

See [`solution.py`](solution.py) for the complete Python solution.

## Repository

**GitHub Repository:** `LeetCode_solution`
