# 0060 - Permutation Sequence

## Problem

The set `[1, 2, 3, ..., n]` contains a total of `n!` unique permutations.

If all permutations are arranged in lexicographical order, we can number them from `1` to `n!`.

Given two integers `n` and `k`, return the **kth permutation sequence**.

## Examples

### Example 1

**Input:**
```text
n = 3
k = 3
```

**Output:**
```text
"213"
```

The permutations are:

```text
1. 123
2. 132
3. 213
4. 231
5. 312
6. 321
```

Therefore, the 3rd permutation is `"213"`.

### Example 2

**Input:**
```text
n = 4
k = 9
```

**Output:**
```text
"2314"
```

### Example 3

**Input:**
```text
n = 3
k = 1
```

**Output:**
```text
"123"
```

## Approach

Instead of generating all `n!` permutations, we directly find the kth permutation using the **factorial number system**.

For example, when `n = 4`, there are:

```text
4! = 24
```

permutations.

The first digit divides the permutations into groups of:

```text
3! = 6
```

So:

```text
1 → permutations 1 to 6
2 → permutations 7 to 12
3 → permutations 13 to 18
4 → permutations 19 to 24
```

We can determine which group contains the kth permutation and select the appropriate number.

We repeat this process for the remaining positions.

## Important Idea

The given `k` is 1-based, so we first convert it to 0-based:

```text
k = k - 1
```

Then we use:

```text
index = k // factorial
```

to determine which remaining number should be selected.

After selecting the number:

```text
k = k % factorial
```

This gives the position inside the selected group.

## Algorithm

1. Create a list containing numbers from `1` to `n`.
2. Calculate `(n - 1)!`.
3. Convert `k` to zero-based indexing by doing `k -= 1`.
4. Find the index of the first number:
   ```text
   index = k // factorial
   ```
5. Add that number to the result and remove it from the list.
6. Update:
   ```text
   k = k % factorial
   ```
7. Divide the factorial by the number of remaining elements.
8. Repeat until all numbers are selected.
9. Return the resulting string.

## Solution

```python
class Solution:
    def getPermutation(self, n, k):
        numbers = [str(i) for i in range(1, n + 1)]

        factorial = 1

        for i in range(1, n):
            factorial *= i

        # Convert k to zero-based indexing
        k -= 1

        result = ""

        while numbers:
            index = k // factorial

            result += numbers.pop(index)

            if not numbers:
                break

            k %= factorial
            factorial //= len(numbers)

        return result
```

## Dry Run

For:

```text
n = 3
k = 3
```

Initially:

```text
numbers = [1, 2, 3]
k = 3
```

Convert `k` to zero-based:

```text
k = 2
```

Calculate:

```text
factorial = 2! = 2
```

### Step 1

```text
index = 2 // 2
      = 1
```

Select:

```text
numbers[1] = 2
```

Result:

```text
"2"
```

Remaining numbers:

```text
[1, 3]
```

Update:

```text
k = 2 % 2 = 0
factorial = 2 // 2 = 1
```

### Step 2

```text
index = 0 // 1
      = 0
```

Select:

```text
1
```

Result:

```text
"21"
```

Remaining:

```text
[3]
```

### Step 3

Select:

```text
3
```

Final result:

```text
"213"
```

Therefore:

```text
Output = "213"
```

## Complexity Analysis

We do not generate all `n!` permutations.

For each position, we remove one element from the list.

- **Time Complexity:** `O(n²)`
- **Space Complexity:** `O(n)`

Since `n <= 9`, this approach is easily fast enough.

## Why We Don't Generate All Permutations

A brute-force approach would generate:

```text
n!
```

permutations.

For `n = 9`:

```text
9! = 362880
```

Generating and storing all permutations is unnecessary.

The factorial-based approach directly calculates the required permutation.

## Key Concept

The important concept used in this problem is the **Factorial Number System**.

The number of permutations beginning with each available number is:

```text
(n - 1)!
```

After selecting one number, the group size becomes:

```text
(n - 2)!
```

and so on.

This allows us to find the kth permutation without generating the previous permutations.

## Edge Cases

### `n = 1`

```text
n = 1
k = 1
```

Output:

```text
"1"
```

### `k = 1`

The first permutation is always the numbers in ascending order.

For example:

```text
n = 4
k = 1
```

Output:

```text
"1234"
```

### `k = n!`

The last permutation is the numbers in descending order.

For example:

```text
n = 4
k = 24
```

Output:

```text
"4321"
```

## Constraints

- `1 <= n <= 9`
- `1 <= k <= n!`

## Language

**Python**

## LeetCode Information

- **Problem Number:** 60
- **Problem Name:** Permutation Sequence
- **Difficulty:** Hard
- **Topics:** Math, Recursion, Combinatorics

## Solution Link

[LeetCode - Permutation Sequence](https://leetcode.com/problems/permutation-sequence/)

## Repository Structure

```text
LeetCode_solution/
│
├── 0001-two-sum/
├── 0002-add-two-numbers/
├── ...
├── 0059-spiral-matrix-ii/
│   ├── README.md
│   └── solution.py
│
└── 0060-permutation-sequence/
    ├── README.md
    └── solution.py
```

## Key Takeaway

Instead of generating every permutation, we use factorial values to determine the correct number at each position.

This makes the solution much more efficient and avoids generating `n!` permutations.
