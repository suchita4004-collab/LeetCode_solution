# Remove Duplicates from Sorted Array II

## Problem

Given an integer array `nums` sorted in **non-decreasing order**, remove duplicates **in-place** so that every unique element appears **at most twice**.

The relative order of the elements must remain the same.

Return `k`, where `k` is the number of elements remaining after removing the extra duplicates.

The first `k` elements of `nums` must contain the final result.

We must use:

```text
O(1) extra space
```

No extra array should be created.

---

## Example 1

**Input:**

```text id="w5m4nq"
nums = [1, 1, 1, 2, 2, 3]
```

**Output:**

```text id="8es1re"
k = 5
nums = [1, 1, 2, 2, 3, _]
```

Each number appears at most twice.

---

## Example 2

**Input:**

```text id="c4c8zz"
nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
```

**Output:**

```text id="9v6n0a"
k = 7
nums = [0, 0, 1, 1, 2, 3, 3, _, _]
```

---

## Approach

We use the **Two Pointer** technique.

Since the array is already sorted, duplicate values are next to each other.

We use two pointers:

- `read` → checks every element.
- `write` → tells us where to place the next valid element.

The first two elements are always allowed because each number can appear **at most twice**.

After that, for every new element, we check:

```text
nums[read] != nums[write - 2]
```

If the current number is different from the number two positions behind the `write` pointer, it is safe to include it.

---

## Why Compare With Two Positions Back?

The important rule is:

> Each number can appear at most twice.

Suppose we have:

```text
[1, 1, 1]
```

After keeping the first two:

```text
[1, 1]
```

When checking the third `1`, we compare it with the element two positions back:

```text
1 == 1
```

So we do not add it.

For:

```text
[1, 1, 2]
```

we check:

```text
2 != 1
```

So `2` can be added.

This simple comparison automatically ensures that no number appears more than twice.

---

## Algorithm

1. If the array has 2 or fewer elements, return its length.
2. Set `write = 2`.
3. Start `read` from index `2`.
4. Compare `nums[read]` with `nums[write - 2]`.
5. If they are different:
   - Copy `nums[read]` to `nums[write]`.
   - Increase `write`.
6. If they are the same, skip the current element.
7. Continue until all elements are checked.
8. Return `write`.

---

## Dry Run

Consider:

```text id="s3eq9k"
nums = [1, 1, 1, 2, 2, 3]
```

Initially:

```text id="w82a7a"
write = 2
```

The first two elements are allowed:

```text id="j84cyx"
[1, 1]
```

### Check third element

```text id="lj5s1w"
read = 2
nums[read] = 1
nums[write - 2] = nums[0] = 1
```

They are equal:

```text id="0l7y3c"
1 == 1
```

So we skip the third `1`.

---

### Check `2`

```text id="bhrq8m"
read = 3
nums[read] = 2
nums[write - 2] = 1
```

They are different:

```text id="3vrz6x"
2 != 1
```

So we keep `2`:

```text id="z4h7cb"
[1, 1, 2]
```

Now:

```text id="8ecf9y"
write = 3
```

---

### Check second `2`

```text id="6k1xw8"
read = 4
nums[read] = 2
nums[write - 2] = nums[1] = 1
```

They are different:

```text id="e0k7eg"
2 != 1
```

Keep it:

```text id="e8a3hd"
[1, 1, 2, 2]
```

---

### Check `3`

```text id="3wqv83"
read = 5
nums[read] = 3
nums[write - 2] = 2
```

They are different:

```text id="7y5c3p"
3 != 2
```

Keep it:

```text id="6i7n1m"
[1, 1, 2, 2, 3]
```

Final:

```text id="0a5x3r"
k = 5
```

The first five positions contain:

```text id="lq8s4j"
[1, 1, 2, 2, 3]
```

---

## How the Code Works

### 1. Handle small arrays

```python id="z7v5n2"
if len(nums) <= 2:
    return len(nums)
```

If there are one or two elements, both can remain because duplicates are allowed twice.

---

### 2. Start the write pointer

```python id="zpm7vp"
write = 2
```

The first two elements are already valid.

So the next valid element will be placed at index `2`.

---

### 3. Read every remaining element

```python id="8v3d2r"
for read in range(2, len(nums)):
```

The `read` pointer checks each element from the third element onward.

---

### 4. Check whether the element should be kept

```python id="1e4u3m"
if nums[read] != nums[write - 2]:
```

If the current element is different from the element two positions behind the write pointer, we can keep it.

---

### 5. Place the valid element

```python id="0t7a6j"
nums[write] = nums[read]
write += 1
```

The element is copied into the correct position.

The array is modified **in-place**.

---

### 6. Return the new length

```python id="1sqx9f"
return write
```

`write` represents how many valid elements are present.

---

## Important Difference From LeetCode #26

### #26 Remove Duplicates from Sorted Array

Each element can appear:

```text
at most once
```

### #80 Remove Duplicates from Sorted Array II

Each element can appear:

```text
at most twice
```

Example:

```text
Original:
[1, 1, 1, 2, 2, 3]

#26:
[1, 2, 3]

#80:
[1, 1, 2, 2, 3]
```

---

## Important Edge Cases

### Case 1: One Element

```text id="h4eh9n"
nums = [1]
```

Output:

```text id="9vyp17"
k = 1
```

---

### Case 2: Two Equal Elements

```text id="y9ryhc"
nums = [2, 2]
```

Output:

```text id="a0c1q7"
k = 2
```

Both elements are allowed.

---

### Case 3: All Elements Are the Same

```text id="8cc2qp"
nums = [5, 5, 5, 5]
```

Output:

```text id="f3q2ap"
k = 2
nums = [5, 5, _, _]
```

Only two copies are kept.

---

### Case 4: No Duplicates

```text id="3m5w6y"
nums = [1, 2, 3, 4]
```

Output:

```text id="u7q3kt"
k = 4
```

Nothing needs to be removed.

---

### Case 5: Many Duplicates

```text id="q6m1q4"
nums = [0, 0, 0, 0, 1, 1, 2]
```

Result:

```text id="xq6s0h"
[0, 0, 1, 1, 2]
```

---

## In-Place Requirement

The problem says that we should not create another array.

Our code does not create a new array.

Instead, it overwrites the original array:

```python id="v9yrgk"
nums[write] = nums[read]
```

Only two integer variables are used:

```text id="u7n0d5"
read
write
```

Therefore, the extra space is constant.

---

## Complexity Analysis

Let `n` be the length of `nums`.

### Time Complexity

```text id="v4c0dp"
O(n)
```

We go through the array only once.

### Space Complexity

```text id="g5l6q8"
O(1)
```

No extra array or data structure is used.

---

## Key Concept

The main concept used is:

**Two Pointers**

The pointers work like this:

```text
read
 ↓
[1, 1, 1, 2, 2, 3]
 ↑
write
```

- `read` scans the array.
- `write` stores valid elements.

The key condition is:

```python id="v4w7tr"
nums[read] != nums[write - 2]
```

This ensures that each value appears **at most twice**.

---

## Constraints

- `1 <= nums.length <= 3 * 10^4`
- `-10^4 <= nums[i] <= 10^4`
- `nums` is sorted in non-decreasing order.
- The array must be modified in-place.
- Extra space must be `O(1)`.

---

## Language

**Python**

---

## LeetCode Information

- **Problem:** Remove Duplicates from Sorted Array II
- **Problem Number:** 80
- **Difficulty:** Medium
- **Topics:** Array, Two Pointers

---

## File Structure

```text id="y2e7kq"
LeetCode_solution/
│
├── 80-remove-duplicates-from-sorted-array-ii/
│   ├── solution.py
│   └── README.md
│
└── README.md
```

---

## Solution Link

[View Solution](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/80-remove-duplicates-from-sorted-array-ii/solution.py)

## Repository Link

[LeetCode_solution](https://github.com/suchita4004-collab/LeetCode_solution)
