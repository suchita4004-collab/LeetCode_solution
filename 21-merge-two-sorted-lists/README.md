# Merge Two Sorted Lists

Given the heads of two sorted linked lists `list1` and `list2`, merge the two lists into one sorted linked list.

The new list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

## Example 1

**Input**

```text id="w8c3vl"
list1 = [1,2,4]
list2 = [1,3,4]
```

### Output

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/21-merge-two-sorted-lists/README.md#output)

```text id="0w3w1q"
[1,1,2,3,4,4]
```

### Explanation

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/21-merge-two-sorted-lists/README.md#explanation)

Both lists are already sorted.

We compare the elements of both lists and connect the smaller node to the merged list.

The final sorted list is:

`1 → 1 → 2 → 3 → 4 → 4`

## Example 2

**Input**

```text id="r6m3zi"
list1 = []
list2 = []
```

### Output

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/21-merge-two-sorted-lists/README.md#output)

```text id="8p3j1z"
[]
```

### Explanation

Both lists are empty, so the merged list is also empty.

## Example 3

**Input**

```text id="m7t4qf"
list1 = []
list2 = [0]
```

### Output

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/21-merge-two-sorted-lists/README.md#output)

```text id="z7l1wp"
[0]
```

### Explanation

The first list is empty, so we return the second list.

## Approach

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/21-merge-two-sorted-lists/README.md#approach)

I use a dummy node and a pointer called `current` to build the merged list.

First, I compare the values of the current nodes of both lists.

If `list1` has the smaller value, I add that node to the merged list. Otherwise, I add the node from `list2`.

I continue this process until one of the lists becomes empty.

Finally, I connect the remaining nodes of the non-empty list to the merged list.

The dummy node makes it easier to handle the first node of the merged list.

## Complexity

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/21-merge-two-sorted-lists/README.md#complexity)

- Time Complexity: O(n + m)
- Space Complexity: O(1)

Where `n` and `m` are the lengths of `list1` and `list2`.

## Solution

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/21-merge-two-sorted-lists/README.md#solution)

[View Solution](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/21-merge-two-sorted-lists/solution.py)
