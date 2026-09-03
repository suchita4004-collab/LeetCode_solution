# Swap Nodes in Pairs

## Problem

Given a linked list, swap every two adjacent nodes and return its head.

The values inside the nodes must not be modified. Only the nodes themselves can be changed.

## Example 1

**Input**

```text
head = [1,2,3,4]
```

### Output

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/24-swap-nodes-in-pairs/README.md#output)

```text
[2,1,4,3]
```

### Explanation

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/24-swap-nodes-in-pairs/README.md#explanation)

The first two nodes `1` and `2` are swapped.

Then the next two nodes `3` and `4` are swapped.

```text
1 → 2 → 3 → 4

2 → 1 → 4 → 3
```

## Example 2

**Input**

```text
head = []
```

### Output

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/24-swap-nodes-in-pairs/README.md#output)

```text
[]
```

### Explanation

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/24-swap-nodes-in-pairs/README.md#explanation)

The linked list is empty, so there is nothing to swap.

## Example 3

**Input**

```text
head = [1]
```

### Output

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/24-swap-nodes-in-pairs/README.md#output)

```text
[1]
```

### Explanation

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/24-swap-nodes-in-pairs/README.md#explanation)

There is only one node, so it remains unchanged.

## Example 4

**Input**

```text
head = [1,2,3]
```

### Output

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/24-swap-nodes-in-pairs/README.md#output)

```text
[2,1,3]
```

### Explanation

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/24-swap-nodes-in-pairs/README.md#explanation)

The first two nodes are swapped.

The last node has no pair, so it remains unchanged.

```text
1 → 2 → 3

2 → 1 → 3
```

## Approach

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/24-swap-nodes-in-pairs/README.md#approach)

I use a **dummy node** and a pointer called `current`.

For every pair of adjacent nodes:

1. Store the first node in `first`.
2. Store the second node in `second`.
3. Connect the first node to the node after the second node.
4. Connect the second node to the first node.
5. Connect the previous node to the second node.
6. Move `current` to the first node of the swapped pair.

This changes only the links between nodes and does not modify their values.

## Complexity

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/24-swap-nodes-in-pairs/README.md#complexity)

- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Solution

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/24-swap-nodes-in-pairs/README.md#solution)

[View Solution](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/24-swap-nodes-in-pairs/solution.py)

## Folder Structure

```text
24-swap-nodes-in-pairs/
├── README.md
└── solution.py
```
