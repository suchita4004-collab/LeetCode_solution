```markdown
# 88. Merge Sorted Array

**Difficulty:** Easy  
**Language:** Python

## Problem

You are given two integer arrays `nums1` and `nums2`, both sorted in non-decreasing order.

You are also given two integers:

- `m` = number of valid elements in `nums1`
- `n` = number of elements in `nums2`

The last `n` positions of `nums1` are empty spaces represented by `0`.

Merge both arrays into `nums1` so that the final array is sorted in non-decreasing order.

---

## Example 1

```text
Input:
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

Output:
[1,2,2,3,5,6]
```

## Example 2

```text
Input:
nums1 = [1]
m = 1
nums2 = []
n = 0

Output:
[1]
```

## Example 3

```text
Input:
nums1 = [0]
m = 0
nums2 = [1]
n = 1

Output:
[1]
```

---

## Approach

We use the **Two Pointer** technique.

Instead of starting from the beginning, we start from the end of both arrays.

We use three pointers:

```text
i = last valid element of nums1
j = last element of nums2
k = last position of nums1
```

We compare the elements at `i` and `j`.

The larger element is placed at position `k`.

Then we move the corresponding pointer backward.

---

## Why Start From the End?

The last `n` positions of `nums1` are empty.

Therefore, we can safely place the largest elements there without overwriting the existing elements.

```text
nums1 = [1,2,3,0,0,0]
             ↑     ↑
             i     k

nums2 = [2,5,6]
            ↑
            j
```

---

## Algorithm

1. Set `i = m - 1`.
2. Set `j = n - 1`.
3. Set `k = m + n - 1`.
4. Compare `nums1[i]` and `nums2[j]`.
5. Place the larger value at `nums1[k]`.
6. Move the corresponding pointer backward.
7. Move `k` backward.
8. Continue until one array is completely processed.
9. If elements are remaining in `nums2`, copy them into `nums1`.

---

## Code

```python
class Solution:
    def merge(self, nums1, m, nums2, n):
        i = m - 1
        j = n - 1
        k = m + n - 1

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1

            k -= 1

        # Copy remaining elements of nums2
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
```

---

## Dry Run

Consider:

```text
nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]

m = 3
n = 3
```

Initial values:

```text
i = 2
j = 2
k = 5
```

### Step 1

Compare:

```text
nums1[i] = 3
nums2[j] = 6
```

`6` is larger.

```text
nums1 = [1,2,3,0,0,6]
```

### Step 2

Compare:

```text
3 and 5
```

Place `5`.

```text
nums1 = [1,2,3,0,5,6]
```

### Step 3

Compare:

```text
3 and 2
```

Place `3`.

```text
nums1 = [1,2,3,3,5,6]
```

### Step 4

Compare:

```text
2 and 2
```

Place `2` from `nums2`.

```text
nums1 = [1,2,2,3,5,6]
```

The remaining elements are already in their correct positions.

### Final Output

```text
[1,2,2,3,5,6]
```

---

## Important Edge Cases

### `nums2` is empty

```text
nums1 = [1]
nums2 = []
```

Result:

```text
[1]
```

### `nums1` has no valid elements

```text
nums1 = [0]
m = 0

nums2 = [1]
n = 1
```

Result:

```text
[1]
```

### Duplicate values

```text
nums1 = [1,2,2,0,0]
nums2 = [2,3]
```

Result:

```text
[1,2,2,2,3]
```

---

## Complexity Analysis

### Time Complexity

```text
O(m + n)
```

Each element is processed at most once.

### Space Complexity

```text
O(1)
```

No extra array is used.

---

## Key Concept

The main idea is:

> **Merge the arrays from the end so that existing elements in `nums1` are not overwritten.**

This allows us to perform the merge **in-place**.

---

## Constraints

- `nums1.length == m + n`
- `nums2.length == n`
- `0 <= m, n <= 200`
- `1 <= m + n <= 200`
- `-10^9 <= nums1[i], nums2[j] <= 10^9`

---

## LeetCode Information

- **Problem:** 88. Merge Sorted Array
- **Difficulty:** Easy
- **Language:** Python
- **Topics:** Array, Two Pointers, Sorting

---

## File Structure

```text
88-merge-sorted-array/
│
├── README.md
└── solution.py
```

---

## Solution

[View solution.py](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/88-merge-sorted-array/solution.py)

## Repository

[LeetCode Solution Repository](https://github.com/suchita4004-collab/LeetCode_solution)
```
