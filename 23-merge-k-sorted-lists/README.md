# Merge k Sorted Lists

## Problem

You are given an array of `k` linked lists.

Each linked list is sorted in ascending order.

Merge all the linked lists into one sorted linked list and return its head.

## Example 1

**Input**

```text
lists = [[1,4,5],[1,3,4],[2,6]]
```

### Output

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/23-merge-k-sorted-lists/README.md#output)

```text
[1,1,2,3,4,4,5,6]
```

### Explanation

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/23-merge-k-sorted-lists/README.md#explanation)

The linked lists are:

```text
1 → 4 → 5
1 → 3 → 4
2 → 6
```

After merging all the lists, the sorted linked list is:

```text
1 → 1 → 2 → 3 → 4 → 4 → 5 → 6
```

## Example 2

**Input**

```text
lists = []
```

### Output

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/23-merge-k-sorted-lists/README.md#output)

```text
[]
```

### Explanation

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/23-merge-k-sorted-lists/README.md#explanation)

There are no linked lists, so the result is an empty list.

## Example 3

**Input**

```text
lists = [[]]
```

### Output

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/23-merge-k-sorted-lists/README.md#output)

```text
[]
```

### Explanation

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/23-merge-k-sorted-lists/README.md#explanation)

The given linked list is empty, so the result is also empty.

## Approach

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/23-merge-k-sorted-lists/README.md#approach)

I use a **min heap** to efficiently find the smallest node among all the linked lists.

First, I add the first node of every non-empty linked list to the heap.

The heap always keeps the node with the smallest value at the top.

1. Remove the smallest node from the heap.
2. Add that node to the merged linked list.
3. If the removed node has a next node, add the next node to the heap.
4. Continue until the heap becomes empty.

The extra index stored in the heap helps distinguish nodes when two nodes have the same value.

## Complexity

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/23-merge-k-sorted-lists/README.md#complexity)

Let `N` be the total number of nodes across all linked lists and `k` be the number of linked lists.

- **Time Complexity:** O(N log k)
- **Space Complexity:** O(k)

The heap contains at most one node from each linked list at a time.

## Solution

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/23-merge-k-sorted-lists/README.md#solution)

[View Solution](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/23-merge-k-sorted-lists/solution.py)

## Folder Structure

```text
23-merge-k-sorted-lists/
├── README.md
└── solution.py
```
