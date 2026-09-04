# Merge k Sorted Lists

## Problem

You are given an array of `k` linked lists.

Each linked list is sorted in ascending order.

Merge all the linked lists into one sorted linked list and return the head of the merged list.

The nodes of the original linked lists should be reused.

## Example 1

**Input**

```text id="m3s6qt"
lists = [[1,4,5],[1,3,4],[2,6]]
```

### Output

```text id="6s7k5m"
[1,1,2,3,4,4,5,6]
```

### Explanation

The linked lists are:

```text id="4x8c5w"
1 -> 4 -> 5
1 -> 3 -> 4
2 -> 6
```

After merging them, the sorted linked list is:

```text id="8l4n2p"
1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6
```

## Example 2

**Input**

```text id="6k8j4r"
lists = []
```

### Output

```text id="7n2p6x"
[]
```

### Explanation

There are no linked lists, so the result is an empty list.

## Example 3

**Input**

```text id="h4s9qy"
lists = [[]]
```

### Output

```text id="u5k1az"
[]
```

### Explanation

The only linked list is empty, so the result is also empty.

## Approach

I use a **min-heap** to efficiently find the smallest node among all the linked lists.

First, I add the first node of every non-empty linked list to the heap.

For every node in the heap:

1. Remove the node with the smallest value.
2. Add that node to the merged linked list.
3. If the removed node has a next node, add the next node to the heap.
4. Continue until the heap becomes empty.

The heap always contains at most one current node from each linked list.

This allows us to efficiently merge all the sorted linked lists.

## Complexity

Let `N` be the total number of nodes and `k` be the number of linked lists.

- **Time Complexity:** O(N log k)
- **Space Complexity:** O(k)

The heap stores at most one node from each linked list.

## Solution

[View Solution](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/0023-merge-k-sorted-lists/solution.py)

## Folder Structure

```text id="q7m2kd"
0023-merge-k-sorted-lists/
├── README.md
└── solution.py
```
