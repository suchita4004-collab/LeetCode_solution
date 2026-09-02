````markdown
# Remove Nth Node From End of List

Given the head of a linked list, remove the `nth` node from the end of the list and return the head of the modified list.

The solution should work in one pass.

## Example 1

```text
Input: head = [1,2,3,4,5], n = 2

Output: [1,2,3,5]
````

### Explanation

The 2nd node from the end is `4`, so we remove it.

The resulting list is:

`1 → 2 → 3 → 5`

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/19-remove-nth-node-from-end-of-list/README.md#example-1)

## Example 2

```text
Input: head = [1], n = 1

Output: []
```

### Explanation

There is only one node, so removing the 1st node from the end makes the list empty.

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/19-remove-nth-node-from-end-of-list/README.md#example-2)

## Example 3

```text
Input: head = [1,2], n = 1

Output: [1]
```

### Explanation

The 1st node from the end is `2`, so we remove it.

The resulting list is:

`1`

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/19-remove-nth-node-from-end-of-list/README.md#example-3)

## Approach

We use the **two-pointer technique** with `fast` and `slow` pointers.

1. Create a dummy node before the head. This makes it easier to handle the case where the first node needs to be removed.
2. Move the `fast` pointer `n` positions forward.
3. Move both `fast` and `slow` pointers together until `fast` reaches the last node.
4. At this point, `slow.next` is the node that needs to be removed.
5. Skip that node using:
   `slow.next = slow.next.next`
6. Return `dummy.next` as the new head.

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/19-remove-nth-node-from-end-of-list/README.md#approach)

## Complexity

* **Time Complexity:** O(n)
* **Space Complexity:** O(1)

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/19-remove-nth-node-from-end-of-list/README.md#complexity)

## Solution

19-remove-nth-node-from-end-of-list/solution.py
19-remove-nth-node-from-end-of-list/README.md



```
```
