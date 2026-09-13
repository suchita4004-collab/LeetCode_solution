```markdown
# 90. Subsets II

**Difficulty:** Medium  
**Language:** Python

## Problem

Given an integer array `nums` that may contain duplicate values, return all possible subsets of the array.

The solution must **not contain duplicate subsets**.

The order of the subsets does not matter.

A subset can contain:

- No elements: `[]`
- One element
- Multiple elements
- All elements

The set of all possible subsets is called the **Power Set**.

---

## Examples

### Example 1

```text
Input:
nums = [1,2,2]

Output:
[[],[1],[1,2],[1,2,2],[2],[2,2]]
```

There are no duplicate subsets in the answer.

### Example 2

```text
Input:
nums = [0]

Output:
[[],[0]]
```

---

## Approach

We use **Backtracking** to generate all possible subsets.

The important part of this problem is handling duplicate values.

First, we sort the array:

```text
[1,2,2]
```

After sorting, duplicate values come next to each other.

Then, while generating subsets, we skip a duplicate value if it occurs at the **same recursion level**.

For example:

```text
[1,2,2]
   ↑ ↑
   same values
```

We allow the second `2` when it is part of a different subset, but we do not start another identical subset from the same level.

---

## Why Do We Sort the Array?

Sorting makes duplicate values adjacent.

For example:

```text
Before sorting:
[2,1,2]

After sorting:
[1,2,2]
```

Now it is easy to check:

```python
nums[i] == nums[i - 1]
```

and skip duplicate choices.

---

## Algorithm

1. Sort the array.
2. Create an empty list `result` to store all subsets.
3. Create an empty list `current` for the current subset.
4. Use a recursive `backtrack()` function.
5. Add the current subset to `result`.
6. Try each element from the current starting position.
7. If the element is a duplicate at the same recursion level, skip it.
8. Add the element to `current`.
9. Recursively generate the remaining subsets.
10. Remove the last element using backtracking.
11. Return `result`.

---

## Code

```python
class Solution:
    def subsetsWithDup(self, nums):
        nums.sort()

        result = []
        current = []

        def backtrack(start):
            # Add the current subset
            result.append(current[:])

            for i in range(start, len(nums)):

                # Skip duplicate elements at the same level
                if i > start and nums[i] == nums[i - 1]:
                    continue

                current.append(nums[i])

                # Generate subsets using the next elements
                backtrack(i + 1)

                # Remove the last element
                current.pop()

        backtrack(0)

        return result
```

---

## Dry Run

Consider:

```text
nums = [1,2,2]
```

After sorting:

```text
[1,2,2]
```

Start with:

```text
current = []
```

Add it to the result:

```text
[]
```

### Choose 1

```text
current = [1]
```

Add:

```text
[1]
```

Now choose the first `2`:

```text
current = [1,2]
```

Add:

```text
[1,2]
```

Choose the second `2`:

```text
current = [1,2,2]
```

Add:

```text
[1,2,2]
```

Backtrack.

Now return to:

```text
[1]
```

The second `2` at the same level is skipped because it is a duplicate.

Next, backtrack to:

```text
[]
```

Now choose `2`:

```text
[2]
```

Add:

```text
[2]
```

Choose the next `2`:

```text
[2,2]
```

Add:

```text
[2,2]
```

Final result:

```text
[[],[1],[1,2],[1,2,2],[2],[2,2]]
```

---

## How Duplicate Values Are Handled

The most important line is:

```python
if i > start and nums[i] == nums[i - 1]:
    continue
```

Suppose:

```text
nums = [1,2,2]
```

At the same recursion level, the two `2`s would create the same subset.

So we skip the second `2`.

However, when the first `2` has already been selected, we are allowed to select the second `2`.

Therefore:

```text
[2]
```

and:

```text
[2,2]
```

are both included.

But we do not generate `[2]` twice.

---

## Backtracking

Backtracking works like this:

```text
Choose
  ↓
Explore
  ↓
Remove
  ↓
Choose another
```

For example:

```text
[]
├── [1]
│   ├── [1,2]
│   │   └── [1,2,2]
│
└── [2]
    └── [2,2]
```

This allows us to generate every unique subset.

---

## Why `current[:]` Is Used

We use:

```python
result.append(current[:])
```

instead of:

```python
result.append(current)
```

because `current` keeps changing during backtracking.

`current[:]` creates a copy of the current subset and stores that fixed version in `result`.

---

## Important Edge Cases

### 1. Array contains one element

```text
Input:
[0]

Output:
[[],[0]]
```

### 2. Array contains duplicates

```text
Input:
[2,2]

Output:
[[],[2],[2,2]]
```

The subset `[2]` appears only once.

### 3. All elements are the same

```text
Input:
[1,1,1]

Output:
[[],[1],[1,1],[1,1,1]]
```

Duplicate subsets are removed.

### 4. Negative numbers

The solution also works with negative values.

```text
Input:
[-1,0,0]

Possible output:
[[],[-1],[-1,0],[-1,0,0],[0],[0,0]]
```

---

## Complexity Analysis

There can be up to `2^n` possible subsets.

### Time Complexity

```text
O(n × 2^n)
```

We may generate up to `2^n` subsets, and copying each subset can take up to `O(n)` time.

### Space Complexity

```text
O(n)
```

for the recursion and current subset, excluding the output.

The output itself can contain up to:

```text
O(n × 2^n)
```

elements.

---

## Key Concept

The main idea is:

> **Sort the array and use backtracking while skipping duplicate elements at the same recursion level.**

The condition:

```python
if i > start and nums[i] == nums[i - 1]:
    continue
```

is what prevents duplicate subsets.

---

## Difference Between Subsets and Subsets II

### Subsets

The input contains unique elements.

Example:

```text
[1,2,3]
```

All `2^3 = 8` subsets are unique.

### Subsets II

The input may contain duplicates.

Example:

```text
[1,2,2]
```

Some subsets would be repeated if we did not handle duplicates.

Therefore, we sort the array and skip duplicate choices.

---

## Constraints

- `1 <= nums.length <= 10`
- `-10 <= nums[i] <= 10`
- `nums` may contain duplicate values.
- The answer must not contain duplicate subsets.

---

## LeetCode Information

- **Problem:** 90. Subsets II
- **Difficulty:** Medium
- **Language:** Python
- **Topics:** Array, Backtracking, Bit Manipulation

---

## File Structure

```text
90-subsets-ii/
│
├── README.md
└── solution.py
```

---

## Solution

[View solution.py](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/90-subsets-ii/solution.py)

## Repository

[LeetCode Solution Repository](https://github.com/suchita4004-collab/LeetCode_solution)
```
