# Subsets

## Problem

Given an integer array `nums` containing **unique elements**, return all possible subsets of `nums`.

A subset is also called part of the **power set**.

The solution must not contain duplicate subsets.

You can return the subsets in any order.

---

## Example 1

**Input:**

```text
nums = [1, 2, 3]
```

**Output:**

```text
[
    [],
    [1],
    [1, 2],
    [1, 2, 3],
    [1, 3],
    [2],
    [2, 3],
    [3]
]
```

There are `2^3 = 8` possible subsets.

---

## Example 2

**Input:**

```text
nums = [0]
```

**Output:**

```text
[
    [],
    [0]
]
```

---

## Approach

We use **Backtracking**.

For every number, we have two possible choices:

1. Include it in the subset.
2. Do not include it in the subset.

For example:

```text
nums = [1, 2, 3]
```

Some possible subsets are:

```text
[]
[1]
[2]
[3]
[1, 2]
[1, 3]
[2, 3]
[1, 2, 3]
```

We start with an empty subset and recursively add numbers.

---

## Backtracking Tree

For:

```text
nums = [1, 2, 3]
```

The subsets can be generated like this:

```text
[]
├── [1]
│   ├── [1, 2]
│   │   └── [1, 2, 3]
│   └── [1, 3]
├── [2]
│   └── [2, 3]
└── [3]
```

Every node represents one valid subset.

Therefore, we add the current subset to the result during every recursive call.

---

## Algorithm

1. Create an empty list `result`.
2. Create an empty list `current`.
3. Start backtracking from index `0`.
4. Add the current subset to `result`.
5. Try adding each remaining number to `current`.
6. Recursively generate further subsets.
7. Remove the last number using `pop()` to backtrack.
8. Continue until all possible subsets are generated.
9. Return `result`.

---

## How the Code Works

### 1. Create result and current lists

```python
result = []
current = []
```

- `result` stores all possible subsets.
- `current` stores the subset currently being built.

---

### 2. Backtracking function

```python
def backtrack(start):
```

The `start` index tells us where to begin choosing the next element.

---

### 3. Save the current subset

```python
result.append(current[:])
```

Every current combination is a valid subset.

We use:

```python
current[:]
```

to create a copy of `current`.

This is important because `current` changes during backtracking.

---

### 4. Try every remaining element

```python
for i in range(start, len(nums)):
```

We choose each remaining number one by one.

---

### 5. Choose an element

```python
current.append(nums[i])
```

For example:

```text
current = [1]
```

Then choosing `2` gives:

```text
current = [1, 2]
```

---

### 6. Explore further subsets

```python
backtrack(i + 1)
```

We continue from the next index.

This ensures that the same element is not selected again.

---

### 7. Backtrack

```python
current.pop()
```

After exploring one possibility, remove the last element and try another choice.

The main backtracking pattern is:

```text
Choose
   ↓
Explore
   ↓
Undo
```

In code:

```python
current.append(nums[i])
backtrack(i + 1)
current.pop()
```

---

## Dry Run

Consider:

```text
nums = [1, 2, 3]
```

Initially:

```text
current = []
result = []
```

### Step 1

Save the empty subset:

```text
result = [[]]
```

Choose `1`:

```text
current = [1]
```

Save it:

```text
result = [[], [1]]
```

Choose `2`:

```text
current = [1, 2]
```

Save it:

```text
result = [[], [1], [1, 2]]
```

Choose `3`:

```text
current = [1, 2, 3]
```

Save it:

```text
result = [[], [1], [1, 2], [1, 2, 3]]
```

Backtrack and explore the remaining possibilities:

```text
[1, 3]
[2]
[2, 3]
[3]
```

Final result:

```text
[
    [],
    [1],
    [1, 2],
    [1, 2, 3],
    [1, 3],
    [2],
    [2, 3],
    [3]
]
```

---

## Number of Subsets

For an array containing `n` unique elements:

```text
Total subsets = 2^n
```

This is because every element has two choices:

```text
Include
or
Exclude
```

For example:

```text
n = 3
```

So:

```text
2^3 = 8 subsets
```

---

## Complexity Analysis

Let `n` be the length of `nums`.

### Time Complexity

```text
O(n × 2^n)
```

There are `2^n` possible subsets.

Copying each subset can take up to `O(n)` time.

### Space Complexity

```text
O(n)
```

excluding the output, because the recursion depth and `current` subset can contain at most `n` elements.

Including the output:

```text
O(n × 2^n)
```

because all subsets are stored.

---

## Important Edge Cases

### Case 1: Single Element

```text
nums = [0]
```

Output:

```text
[[], [0]]
```

### Case 2: All Elements Are Unique

The problem guarantees that all elements are unique.

Therefore, duplicate subsets are not generated.

### Case 3: Negative Numbers

```text
nums = [-1, 0, 1]
```

The same backtracking approach works correctly.

---

## Key Concept

The main concept used is:

**Backtracking**

The pattern is:

```text
Add current subset
       ↓
Choose an element
       ↓
Explore recursively
       ↓
Remove the element
       ↓
Try another choice
```

The core code is:

```python
result.append(current[:])

for i in range(start, len(nums)):
    current.append(nums[i])
    backtrack(i + 1)
    current.pop()
```

---

## Constraints

- `1 <= nums.length <= 10`
- `-10 <= nums[i] <= 10`
- All elements in `nums` are unique.

---

## Language

**Python**

---

## LeetCode Information

- **Problem:** Subsets
- **Problem Number:** 78
- **Difficulty:** Medium
- **Topics:** Array, Backtracking, Bit Manipulation

---

## File Structure

```text
LeetCode_solution/
│
├── 78-subsets/
│   ├── solution.py
│   └── README.md
│
└── README.md
```

---

## Solution Link

[View Solution](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/78-subsets/solution.py)

## Repository Link

[LeetCode_solution](https://github.com/suchita4004-collab/LeetCode_solution)
