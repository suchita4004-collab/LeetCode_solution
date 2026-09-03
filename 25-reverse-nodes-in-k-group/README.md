# Reverse Nodes in k-Group

## Problem

Given the head of a linked list, reverse the nodes of the list `k` at a time and return the modified list.

If the number of nodes is not a multiple of `k`, the remaining nodes at the end should stay in their original order.

The values of the nodes must not be changed. Only the connections between nodes can be changed.

## Example 1

**Input**

```text
head = [1,2,3,4,5]
k = 2
```

### Output

```text
[2,1,4,3,5]
```

### Explanation

The linked list is divided into groups of 2:

```text
1 → 2    3 → 4    5
```

Reverse each complete group:

```text
2 → 1    4 → 3    5
```

The last node remains unchanged because it does not form a complete group of 2.

## Example 2

**Input**

```text
head = [1,2,3,4,5]
k = 3
```

### Output

```text
[3,2,1,4,5]
```

### Explanation

The first three nodes form a complete group:

```text
1 → 2 → 3
```

After reversing:

```text
3 → 2 → 1
```

The remaining nodes `4 → 5` are left unchanged because there are fewer than 3 nodes.

## Approach

I use a dummy node and reverse the linked list one group at a time.

For each group:

1. Find the `k`th node from the current position.
2. If there are fewer than `k` nodes remaining, return the list without reversing them.
3. Store the node after the group.
4. Reverse all nodes in the current group.
5. Connect the reversed group with the previous and next parts of the list.
6. Move to the next group.

The node values are never changed. Only the `next` pointers are modified.

## Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Solution

[View Solution](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/25-reverse-nodes-in-k-group/solution.py)

## Folder Structure

```text
25-reverse-nodes-in-k-group/
├── README.md
└── solution.py
```
