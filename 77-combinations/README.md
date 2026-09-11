# Combinations

## Problem

Given two integers `n` and `k`, return all possible combinations of `k` numbers chosen from the range:

```text
[1, n]
```

Each number can be selected only once.

The order does not matter.

For example:

```text
[1, 2]
```

and

```text
[2, 1]
```

are considered the same combination.

---

## Example 1

**Input:**

```text
n = 4
k = 2
```

**Output:**

```text
[
    [1, 2],
    [1, 3],
    [1, 4],
    [2, 3],
    [2, 4],
    [3, 4]
]
```

There are:

```text
4 choose 2 = 6
```

possible combinations.

---

## Example 2

**Input:**

```text
n = 1
k = 1
```

**Output:**

```text
[[1]]
```

---

## Approach

We use **Backtracking**.

Backtracking means:

1. Choose a number.
2. Add it to the current combination.
3. Recursively choose the next number.
4. When the combination contains `k` numbers, save it.
5. Remove the last number and try another possibility.

For:

```text
n = 4
k = 2
```

the choices look like:

```text
                 []
          /       |       |       \
        [1]      [2]     [3]      [4]
       / | \      / \      |
    [1,2][1,3][1,4][2,3][2,4][3,4]
```

We always choose the next number after the current number.

Therefore, `[2,1]` is never generated after `[1,2]`.

---

## Algorithm

1. Create an empty `result` list.
2. Create an empty `current` list.
3. Start backtracking from number `1`.
4. Add a number to `current`.
5. Call backtracking with the next number.
6. When `len(current) == k`, add a copy of `current` to `result`.
7. Remove the last number using `pop()`.
8. Continue trying other numbers.
9. Return `result`.

---

## Dry Run

Consider:

```text
n = 4
k = 2
```

Initially:

```text
current = []
```

### Choose `1`

```text
current = [1]
```

Choose `2`:

```text
current = [1, 2]
```

Two numbers have been selected, so save it:

```text
result = [[1, 2]]
```

Backtrack:

```text
current = [1]
```

Choose `3`:

```text
current = [1, 3]
```

Save:

```text
result = [
    [1, 2],
    [1, 3]
]
```

Choose `4`:

```text
current = [1, 4]
```

Save:

```text
result = [
    [1, 2],
    [1, 3],
    [1, 4]
]
```

Backtrack and choose `2` as the first number:

```text
current = [2]
```

Then:

```text
[2, 3]
[2, 4]
```

Finally:

```text
[3, 4]
```

Final result:

```text
[
    [1, 2],
    [1, 3],
    [1, 4],
    [2, 3],
    [2, 4],
    [3, 4]
]
```

---

## How the Code Works

### 1. Result and current lists

```python
result = []
current = []
```

- `result` stores all completed combinations.
- `current` stores the combination currently being built.

### 2. Backtracking function

```python
def backtrack(start):
```

`start` tells us where we should start looking for the next number.

### 3. Check if combination is complete

```python
if len(current) == k:
    result.append(current[:])
    return
```

When `k` numbers have been selected, we store the combination.

`current[:]` creates a copy so that later changes to `current` do not change the saved result.

### 4. Try available numbers

```python
for num in range(start, n + 1):
```

We try every possible number from `start` to `n`.

### 5. Choose

```python
current.append(num)
```

The number is added to the current combination.

### 6. Recursive call

```python
backtrack(num + 1)
```

We start from `num + 1`.

This prevents duplicate combinations.

For example, after choosing `2`, we only consider:

```text
3, 4, 5, ...
```

We never go back to `1`.

### 7. Backtrack

```python
current.pop()
```

After exploring one choice, we remove it and try another choice.

This is the main idea of backtracking.

---

## Why Do We Use `num + 1`?

Suppose:

```text
current = [1]
```

The next choices can be:

```text
2, 3, 4
```

After choosing `2`:

```text
current = [1, 2]
```

The next number must be greater than `2`.

So we call:

```python
backtrack(3)
```

This guarantees that combinations are generated in increasing order.

Therefore:

```text
[1, 2]
```

is generated, but:

```text
[2, 1]
```

is not generated.

---

## Combination Formula

The total number of combinations is:

```text
C(n, k) = n! / (k! × (n-k)!)
```

For:

```text
n = 4
k = 2
```

we get:

```text
C(4, 2) = 4! / (2! × 2!)
        = 24 / 4
        = 6
```

So there are 6 possible combinations.

genui{"learning_viz":{"type_id":"COMBINATION_FORMULA","initial_values":{"n":4,"r":2}}}

---

## Important Edge Cases

### Case 1: `k = 1`

```text
n = 3
k = 1
```

Output:

```text
[[1], [2], [3]]
```

### Case 2: `k = n`

```text
n = 3
k = 3
```

Output:

```text
[[1, 2, 3]]
```

### Case 3: `n = 1, k = 1`

```text
Output = [[1]]
```

### Case 4: Larger values

The constraints allow:

```text
n <= 20
```

The backtracking approach efficiently generates the required combinations.

---

## Complexity Analysis

Let:

```text
C(n, k) = n! / (k! × (n-k)!)
```

be the number of combinations.

### Time Complexity

Approximately:

```text
O(C(n, k) × k)
```

We generate `C(n, k)` combinations, and each combination contains `k` elements.

### Space Complexity

```text
O(k)
```

for the current backtracking path, excluding the output.

Including the result:

```text
O(C(n, k) × k)
```

because all combinations must be stored.

---

## Key Concept

The main concept used is:

**Backtracking**

The pattern is:

```text
Choose
   ↓
Explore
   ↓
Save if complete
   ↓
Undo choice
   ↓
Try next choice
```

In code:

```python
current.append(num)
backtrack(num + 1)
current.pop()
```

This three-step pattern is very common in combination and permutation problems.

---

## Constraints

- `1 <= n <= 20`
- `1 <= k <= n`

---

## Language

**Python**

---

## LeetCode Information

- **Problem:** Combinations
- **Problem Number:** 77
- **Difficulty:** Medium
- **Topics:** Backtracking, Array

---

## File Structure

```text
LeetCode_solution/
│
├── 77-combinations/
│   ├── solution.py
│   └── README.md
│
└── README.md
```

---

## Solution Link

[View Solution](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/77-combinations/solution.py)

## Repository Link

[LeetCode_solution](https://github.com/suchita4004-collab/LeetCode_solution)
