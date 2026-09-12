# Search in Rotated Sorted Array II

## Problem

Given an integer array `nums` sorted in non-decreasing order, the array is rotated at an unknown position.

The array may contain **duplicate values**.

Given a `target`, return:

- `True` if `target` exists in `nums`
- `False` if `target` does not exist

The goal is to reduce the number of operations as much as possible.

---

## Example 1

**Input:**

```text id="m4c9qa"
nums = [2, 5, 6, 0, 0, 1, 2]
target = 0
```

**Output:**

```text id="9i5t1p"
True
```

The target `0` is present in the array.

---

## Example 2

**Input:**

```text id="0m7z8f"
nums = [2, 5, 6, 0, 0, 1, 2]
target = 3
```

**Output:**

```text id="m9k2q1"
False
```

The target `3` is not present.

---

## Approach

We use **Modified Binary Search**.

Normally, binary search works directly on a sorted array.

However, this array has been rotated.

For example:

```text id="6h0m1q"
Original:
[0, 1, 2, 4, 4, 4, 5, 6, 6, 7]

Rotated:
[4, 5, 6, 6, 7, 0, 1, 2, 4, 4]
```

Even after rotation, at least one side of the middle element is usually sorted.

We determine which side is sorted and then decide where the target can exist.

---

## Important Problem With Duplicates

Duplicates can make it difficult to determine which side is sorted.

For example:

```text id="e0b9av"
[1, 1, 1, 1, 1]
```

Here:

```text id="w9e6rj"
nums[left] == nums[mid] == nums[right]
```

We cannot determine which side contains useful information.

So we safely shrink the search space:

```python id="l8f0nq"
left += 1
right -= 1
```

This handles the duplicate case.

---

## Algorithm

1. Set `left = 0` and `right = len(nums) - 1`.
2. Calculate the middle index.
3. If `nums[mid] == target`, return `True`.
4. Check whether:
   ```text id="7e8p2j"
   nums[left] == nums[mid] == nums[right]
   ```
5. If they are equal, move both pointers inward.
6. Otherwise, determine which half is sorted.
7. If the left half is sorted:
   - Check whether the target lies inside that range.
   - If yes, search the left half.
   - Otherwise, search the right half.
8. If the right half is sorted:
   - Check whether the target lies inside that range.
   - If yes, search the right half.
   - Otherwise, search the left half.
9. Continue until `left > right`.
10. If the target was not found, return `False`.

---

## Dry Run

Consider:

```text id="0w1z3b"
nums = [2, 5, 6, 0, 0, 1, 2]
target = 0
```

Initially:

```text id="5p2k4v"
left = 0
right = 6
```

### Step 1

```text id="zq2k3p"
mid = (0 + 6) // 2
mid = 3
```

So:

```text id="a9x1f5"
nums[mid] = 0
```

Target is `0`.

Therefore:

```text id="w1n4s8"
return True
```

---

## Dry Run for Target Not Found

Consider:

```text id="v5j7k2"
nums = [2, 5, 6, 0, 0, 1, 2]
target = 3
```

### Step 1

```text id="e7b4d1"
left = 0
right = 6
mid = 3
```

Values:

```text id="j5f8p2"
left  = 2
mid   = 0
right = 2
```

The right half is sorted:

```text id="6b3m1x"
[0, 1, 2]
```

Target `3` is not in this range.

So we search the left half:

```text id="q4x9mn"
right = mid - 1
right = 2
```

### Step 2

```text id="j2m6qp"
left = 0
right = 2
mid = 1
```

Values:

```text id="w8n3ka"
[2, 5, 6]
    ↑
   mid
```

The left half is sorted.

Target `3` is not between `2` and `5`.

So:

```text id="s1v5y7"
left = mid + 1
left = 2
```

### Step 3

```text id="f8k2w4"
left = 2
right = 2
mid = 2
```

```text id="0z7x1c"
nums[mid] = 6
```

`6 != 3`.

The search space becomes empty.

Therefore:

```text id="h4p9s2"
return False
```

---

## How the Code Works

### 1. Initialize pointers

```python id="2q6n9v"
left = 0
right = len(nums) - 1
```

These pointers represent the current search range.

---

### 2. Find the middle

```python id="m3x7p1"
mid = (left + right) // 2
```

We check the middle element first.

---

### 3. Check the target

```python id="n8k2q5"
if nums[mid] == target:
    return True
```

If the middle element is the target, the search is complete.

---

### 4. Handle duplicates

```python id="v6m1s9"
if nums[left] == nums[mid] == nums[right]:
    left += 1
    right -= 1
    continue
```

When all three values are equal, we cannot determine which side is sorted.

Removing the duplicate boundary values is safe because they are equal to the middle value, which has already been checked against the target.

---

### 5. Check if the left half is sorted

```python id="k4r8t2"
if nums[left] <= nums[mid]:
```

If this condition is true, the left side is sorted.

For example:

```text id="a3m9x7"
[2, 5, 6]
 ↑     ↑
left  mid
```

---

### 6. Check whether target is in the left half

```python id="p7n2c5"
if nums[left] <= target < nums[mid]:
    right = mid - 1
```

If the target belongs to the sorted left half, we search there.

Otherwise:

```python id="h1v6q8"
left = mid + 1
```

---

### 7. Otherwise, the right half is sorted

```python id="r5x8m3"
else:
```

We know the right half is sorted.

We check whether the target lies between:

```text id="s9q2j4"
nums[mid] and nums[right]
```

If yes:

```python id="a7k3p6"
left = mid + 1
```

Otherwise:

```python id="m2v8n5"
right = mid - 1
```

---

## Example of Duplicate Handling

Consider:

```text id="y8m4q2"
nums = [1, 0, 1, 1, 1]
target = 0
```

At some point we may have:

```text id="x3n7p9"
left = 0
mid = 2
right = 4

nums[left]  = 1
nums[mid]   = 1
nums[right] = 1
```

All three are equal.

We cannot know which side is sorted.

So we do:

```text id="b6k1r5"
left += 1
right -= 1
```

and continue searching.

---

## Why Binary Search Is Better

A simple linear search would check every element:

```text id="v3j8q1"
O(n)
```

Modified binary search usually reduces the search space by half:

```text id="n6p2x9"
O(log n)
```

However, because duplicates can force us to remove only one element from each side, the worst-case complexity becomes:

```text id="k8m4z2"
O(n)
```

---

## Important Edge Cases

### Case 1: One Element

```text id="a2c7v9"
nums = [1]
target = 1
```

Output:

```text id="x5n8q3"
True
```

---

### Case 2: Target Not Present

```text id="p4m7k1"
nums = [1]
target = 2
```

Output:

```text id="r8z2y6"
False
```

---

### Case 3: All Elements Are Equal

```text id="h6q3m8"
nums = [2, 2, 2, 2, 2]
target = 2
```

Output:

```text id="w7k1p4"
True
```

---

### Case 4: All Elements Are Equal but Target Is Different

```text id="b9x4n2"
nums = [2, 2, 2, 2, 2]
target = 3
```

Output:

```text id="c5m8q1"
False
```

---

### Case 5: Rotation With Duplicates

```text id="t2v7k9"
nums = [4, 5, 6, 6, 7, 0, 1, 2, 4, 4]
target = 6
```

Output:

```text id="m3p8x5"
True
```

---

## Complexity Analysis

Let `n` be the length of `nums`.

### Average Time Complexity

```text id="q7m2v5"
O(log n)
```

The search space is normally reduced approximately by half.

### Worst-Case Time Complexity

```text id="r4x8n1"
O(n)
```

When many duplicate values are present, we may only be able to shrink the search range one element from each side.

For example:

```text id="z5k9p3"
[1, 1, 1, 1, 1, 1, 1]
```

### Space Complexity

```text id="v2m6q8"
O(1)
```

Only a few variables are used.

---

## Key Concept

The main concept is:

**Modified Binary Search**

The decision process is:

```text
             Find middle
                  ↓
          Is target found?
             /       \
           Yes        No
            ↓          ↓
         Return    Are boundaries
                    duplicates?
                    /       \
                  Yes        No
                   ↓          ↓
              Shrink      Find sorted
              range         half
                              ↓
                       Choose left/right
                              ↓
                         Continue search
```

The important condition for duplicates is:

```python id="d4w9s2"
if nums[left] == nums[mid] == nums[right]:
    left += 1
    right -= 1
```

---

## Constraints

- `1 <= nums.length <= 5000`
- `-10^4 <= nums[i] <= 10^4`
- `nums` is guaranteed to be rotated.
- `-10^4 <= target <= 10^4`
- Duplicate values are allowed.

---

## Language

**Python**

---

## LeetCode Information

- **Problem:** Search in Rotated Sorted Array II
- **Problem Number:** 81
- **Difficulty:** Medium
- **Topics:** Array, Binary Search

---

## File Structure

```text id="k7n3v9"
LeetCode_solution/
│
├── 81-search-in-rotated-sorted-array-ii/
│   ├── solution.py
│   └── README.md
│
└── README.md
```

---

## Solution Link

[View Solution](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/81-search-in-rotated-sorted-array-ii/solution.py)

## Repository Link

[LeetCode_solution](https://github.com/suchita4004-collab/LeetCode_solution)
