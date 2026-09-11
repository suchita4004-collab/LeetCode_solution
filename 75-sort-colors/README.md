```markdown id="a3x7kp"
# 75 - Sort Colors

## Problem

You are given an array `nums` containing objects of three colors:

- `0` → Red
- `1` → White
- `2` → Blue

Sort the array **in-place** so that the colors appear in this order:

```text
0 → 1 → 2
```

You are **not allowed to use the library's sorting function**.

The solution should modify the original array directly.

---

## Examples

### Example 1

**Input:**
```text
nums = [2,0,2,1,1,0]
```

**Output:**
```text
[0,0,1,1,2,2]
```

**Explanation:**

The array contains:

```text
0 → two times
1 → two times
2 → two times
```

After sorting:

```text
[0,0,1,1,2,2]
```

---

### Example 2

**Input:**
```text
nums = [2,0,1]
```

**Output:**
```text
[0,1,2]
```

**Explanation:**

There is one `0`, one `1`, and one `2`.

They are arranged in the required order.

---

## Approach

We can solve this problem using the **Dutch National Flag Algorithm**.

We use three pointers:

```text
low
mid
high
```

They divide the array into four sections:

```text
0s        1s          unknown          2s
↓         ↓              ↓              ↓
[ 0 0 | 1 1 |   ? ? ?   | 2 2 ]
       low  mid          high
```

The goal is to move:

- All `0`s to the left.
- All `1`s to the middle.
- All `2`s to the right.

---

## Three Pointers

### `low`

Points to the position where the next `0` should be placed.

### `mid`

Points to the current element that we are checking.

### `high`

Points to the position where the next `2` should be placed.

---

## Rules

While `mid <= high`:

### If `nums[mid] == 0`

Move `0` to the beginning.

```text
swap(nums[low], nums[mid])
```

Then:

```text
low += 1
mid += 1
```

---

### If `nums[mid] == 1`

`1` is already in the correct middle section.

So only:

```text
mid += 1
```

---

### If `nums[mid] == 2`

Move `2` to the end.

```text
swap(nums[mid], nums[high])
```

Then:

```text
high -= 1
```

We do **not** increase `mid` here because the new value that came from `high` has not been checked yet.

---

## Algorithm

1. Set `low = 0`.
2. Set `mid = 0`.
3. Set `high = len(nums) - 1`.
4. While `mid <= high`:
   - If current value is `0`, swap it with `low`.
   - If current value is `1`, move `mid`.
   - If current value is `2`, swap it with `high`.
5. Continue until all elements are processed.
6. The array will be sorted as `0, 1, 2`.

---

## Dry Run

Consider:

```text
nums = [2,0,2,1,1,0]
```

Initial:

```text
low = 0
mid = 0
high = 5
```

### Step 1

Current:

```text
nums[mid] = 2
```

Swap with `high`:

```text
[0,0,2,1,1,2]
```

Now:

```text
high = 4
mid = 0
```

---

### Step 2

Current:

```text
nums[mid] = 0
```

Swap with `low`:

```text
[0,0,2,1,1,2]
```

Move:

```text
low = 1
mid = 1
```

---

### Step 3

Current:

```text
nums[mid] = 0
```

Swap with `low`:

```text
[0,0,2,1,1,2]
```

Move:

```text
low = 2
mid = 2
```

---

### Step 4

Current:

```text
nums[mid] = 2
```

Swap with `high`:

```text
[0,0,1,1,2,2]
```

Move:

```text
high = 3
```

`mid` stays at `2`.

---

### Step 5

Current:

```text
nums[mid] = 1
```

`1` is already in the correct section.

```text
mid = 3
```

---

### Step 6

Current:

```text
nums[mid] = 1
```

Again:

```text
mid = 4
```

Now:

```text
mid > high
```

The process stops.

Final array:

```text
[0,0,1,1,2,2]
```

---

## Solution

```python id="j7x2mc"
class Solution:
    def sortColors(self, nums):
        low = 0
        mid = 0
        high = len(nums) - 1

        while mid <= high:

            # 0 should go to the beginning
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1

            # 1 stays in the middle
            elif nums[mid] == 1:
                mid += 1

            # 2 should go to the end
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
```

---

## How the Code Works

### 1. Initialize three pointers

```python id="u4v9pk"
low = 0
mid = 0
high = len(nums) - 1
```

Initially:

```text
low  → beginning
mid  → beginning
high → end
```

---

### 2. Process the array

```python id="r2m6xz"
while mid <= high:
```

We continue until the unknown section becomes empty.

---

### 3. When the value is `0`

```python id="f7q3mn"
if nums[mid] == 0:
    nums[low], nums[mid] = nums[mid], nums[low]
    low += 1
    mid += 1
```

`0` belongs at the beginning.

So we swap it with the element at `low`.

---

### 4. When the value is `1`

```python id="k8p4wd"
elif nums[mid] == 1:
    mid += 1
```

`1` belongs in the middle.

Therefore, no swapping is needed.

---

### 5. When the value is `2`

```python id="s5x9qa"
else:
    nums[mid], nums[high] = nums[high], nums[mid]
    high -= 1
```

`2` belongs at the end.

We swap it with the element at `high`.

Notice that `mid` does **not** increase.

This is important because the new value placed at `mid` still needs to be checked.

---

## Important Edge Cases

### Case 1: Only zeros

```text
Input:
[0,0,0]

Output:
[0,0,0]
```

---

### Case 2: Only ones

```text
Input:
[1,1,1]

Output:
[1,1,1]
```

---

### Case 3: Only twos

```text
Input:
[2,2,2]

Output:
[2,2,2]
```

---

### Case 4: Already sorted

```text
Input:
[0,1,2]

Output:
[0,1,2]
```

---

### Case 5: Reverse order

```text
Input:
[2,1,0]

Output:
[0,1,2]
```

---

### Case 6: Single element

```text
Input:
[1]

Output:
[1]
```

---

## Complexity Analysis

### Time Complexity

```text
O(n)
```

Each element is processed a constant number of times.

### Space Complexity

```text
O(1)
```

The array is modified **in-place** and only three pointers are used.

---

## Key Concept

The main concept used in this problem is the:

**Dutch National Flag Algorithm**

It divides the array into three regions:

```text
+---------+---------+-----------+---------+
|    0    |    1    |  Unknown  |    2    |
+---------+---------+-----------+---------+
     ↑         ↑          ↑           ↑
    low       mid       mid         high
```

The final arrangement is:

```text
0 0 0 0 | 1 1 1 | 2 2 2 2
```

---

## Why Not Use `sort()`?

The problem specifically says:

```text
Do not use the library's sort function.
```

Therefore, we manually rearrange the elements using swaps.

This also gives:

```text
Time  → O(n)
Space → O(1)
```

---

## Constraints

```text
n == nums.length
1 <= n <= 300
nums[i] is either 0, 1, or 2
```

---

## Language

**Python**

---

## LeetCode Information

- **Problem:** Sort Colors
- **Problem Number:** 75
- **Difficulty:** Medium
- **Topic:** Array
- **Pattern:** Two Pointers / Dutch National Flag

---

## File Structure

```text
75-sort-colors/
├── README.md
└── solution.py
```

---

## Solution Link

[View Solution](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/75-sort-colors/solution.py)

---

## Repository Link

[LeetCode_solution](https://github.com/suchita4004-collab/LeetCode_solution)
``````markdown id="a3x7kp"
# 75 - Sort Colors

## Problem

You are given an array `nums` containing objects of three colors:

- `0` → Red
- `1` → White
- `2` → Blue

Sort the array **in-place** so that the colors appear in this order:

```text
0 → 1 → 2
```

You are **not allowed to use the library's sorting function**.

The solution should modify the original array directly.

---

## Examples

### Example 1

**Input:**
```text
nums = [2,0,2,1,1,0]
```

**Output:**
```text
[0,0,1,1,2,2]
```

**Explanation:**

The array contains:

```text
0 → two times
1 → two times
2 → two times
```

After sorting:

```text
[0,0,1,1,2,2]
```

---

### Example 2

**Input:**
```text
nums = [2,0,1]
```

**Output:**
```text
[0,1,2]
```

**Explanation:**

There is one `0`, one `1`, and one `2`.

They are arranged in the required order.

---

## Approach

We can solve this problem using the **Dutch National Flag Algorithm**.

We use three pointers:

```text
low
mid
high
```

They divide the array into four sections:

```text
0s        1s          unknown          2s
↓         ↓              ↓              ↓
[ 0 0 | 1 1 |   ? ? ?   | 2 2 ]
       low  mid          high
```

The goal is to move:

- All `0`s to the left.
- All `1`s to the middle.
- All `2`s to the right.

---

## Three Pointers

### `low`

Points to the position where the next `0` should be placed.

### `mid`

Points to the current element that we are checking.

### `high`

Points to the position where the next `2` should be placed.

---

## Rules

While `mid <= high`:

### If `nums[mid] == 0`

Move `0` to the beginning.

```text
swap(nums[low], nums[mid])
```

Then:

```text
low += 1
mid += 1
```

---

### If `nums[mid] == 1`

`1` is already in the correct middle section.

So only:

```text
mid += 1
```

---

### If `nums[mid] == 2`

Move `2` to the end.

```text
swap(nums[mid], nums[high])
```

Then:

```text
high -= 1
```

We do **not** increase `mid` here because the new value that came from `high` has not been checked yet.

---

## Algorithm

1. Set `low = 0`.
2. Set `mid = 0`.
3. Set `high = len(nums) - 1`.
4. While `mid <= high`:
   - If current value is `0`, swap it with `low`.
   - If current value is `1`, move `mid`.
   - If current value is `2`, swap it with `high`.
5. Continue until all elements are processed.
6. The array will be sorted as `0, 1, 2`.

---

## Dry Run

Consider:

```text
nums = [2,0,2,1,1,0]
```

Initial:

```text
low = 0
mid = 0
high = 5
```

### Step 1

Current:

```text
nums[mid] = 2
```

Swap with `high`:

```text
[0,0,2,1,1,2]
```

Now:

```text
high = 4
mid = 0
```

---

### Step 2

Current:

```text
nums[mid] = 0
```

Swap with `low`:

```text
[0,0,2,1,1,2]
```

Move:

```text
low = 1
mid = 1
```

---

### Step 3

Current:

```text
nums[mid] = 0
```

Swap with `low`:

```text
[0,0,2,1,1,2]
```

Move:

```text
low = 2
mid = 2
```

---

### Step 4

Current:

```text
nums[mid] = 2
```

Swap with `high`:

```text
[0,0,1,1,2,2]
```

Move:

```text
high = 3
```

`mid` stays at `2`.

---

### Step 5

Current:

```text
nums[mid] = 1
```

`1` is already in the correct section.

```text
mid = 3
```

---

### Step 6

Current:

```text
nums[mid] = 1
```

Again:

```text
mid = 4
```

Now:

```text
mid > high
```

The process stops.

Final array:

```text
[0,0,1,1,2,2]
```

---

## Solution

```python id="j7x2mc"
class Solution:
    def sortColors(self, nums):
        low = 0
        mid = 0
        high = len(nums) - 1

        while mid <= high:

            # 0 should go to the beginning
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1

            # 1 stays in the middle
            elif nums[mid] == 1:
                mid += 1

            # 2 should go to the end
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
```

---

## How the Code Works

### 1. Initialize three pointers

```python id="u4v9pk"
low = 0
mid = 0
high = len(nums) - 1
```

Initially:

```text
low  → beginning
mid  → beginning
high → end
```

---

### 2. Process the array

```python id="r2m6xz"
while mid <= high:
```

We continue until the unknown section becomes empty.

---

### 3. When the value is `0`

```python id="f7q3mn"
if nums[mid] == 0:
    nums[low], nums[mid] = nums[mid], nums[low]
    low += 1
    mid += 1
```

`0` belongs at the beginning.

So we swap it with the element at `low`.

---

### 4. When the value is `1`

```python id="k8p4wd"
elif nums[mid] == 1:
    mid += 1
```

`1` belongs in the middle.

Therefore, no swapping is needed.

---

### 5. When the value is `2`

```python id="s5x9qa"
else:
    nums[mid], nums[high] = nums[high], nums[mid]
    high -= 1
```

`2` belongs at the end.

We swap it with the element at `high`.

Notice that `mid` does **not** increase.

This is important because the new value placed at `mid` still needs to be checked.

---

## Important Edge Cases

### Case 1: Only zeros

```text
Input:
[0,0,0]

Output:
[0,0,0]
```

---

### Case 2: Only ones

```text
Input:
[1,1,1]

Output:
[1,1,1]
```

---

### Case 3: Only twos

```text
Input:
[2,2,2]

Output:
[2,2,2]
```

---

### Case 4: Already sorted

```text
Input:
[0,1,2]

Output:
[0,1,2]
```

---

### Case 5: Reverse order

```text
Input:
[2,1,0]

Output:
[0,1,2]
```

---

### Case 6: Single element

```text
Input:
[1]

Output:
[1]
```

---

## Complexity Analysis

### Time Complexity

```text
O(n)
```

Each element is processed a constant number of times.

### Space Complexity

```text
O(1)
```

The array is modified **in-place** and only three pointers are used.

---

## Key Concept

The main concept used in this problem is the:

**Dutch National Flag Algorithm**

It divides the array into three regions:

```text
+---------+---------+-----------+---------+
|    0    |    1    |  Unknown  |    2    |
+---------+---------+-----------+---------+
     ↑         ↑          ↑           ↑
    low       mid       mid         high
```

The final arrangement is:

```text
0 0 0 0 | 1 1 1 | 2 2 2 2
```

---

## Why Not Use `sort()`?

The problem specifically says:

```text
Do not use the library's sort function.
```

Therefore, we manually rearrange the elements using swaps.

This also gives:

```text
Time  → O(n)
Space → O(1)
```

---

## Constraints

```text
n == nums.length
1 <= n <= 300
nums[i] is either 0, 1, or 2
```

---

## Language

**Python**

---

## LeetCode Information

- **Problem:** Sort Colors
- **Problem Number:** 75
- **Difficulty:** Medium
- **Topic:** Array
- **Pattern:** Two Pointers / Dutch National Flag

---

## File Structure

```text
75-sort-colors/
├── README.md
└── solution.py
```

---

## Solution Link

[View Solution](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/75-sort-colors/solution.py)

---

## Repository Link

[LeetCode_solution](https://github.com/suchita4004-collab/LeetCode_solution)
``````markdown id="a3x7kp"
# 75 - Sort Colors

## Problem

You are given an array `nums` containing objects of three colors:

- `0` → Red
- `1` → White
- `2` → Blue

Sort the array **in-place** so that the colors appear in this order:

```text
0 → 1 → 2
```

You are **not allowed to use the library's sorting function**.

The solution should modify the original array directly.

---

## Examples

### Example 1

**Input:**
```text
nums = [2,0,2,1,1,0]
```

**Output:**
```text
[0,0,1,1,2,2]
```

**Explanation:**

The array contains:

```text
0 → two times
1 → two times
2 → two times
```

After sorting:

```text
[0,0,1,1,2,2]
```

---

### Example 2

**Input:**
```text
nums = [2,0,1]
```

**Output:**
```text
[0,1,2]
```

**Explanation:**

There is one `0`, one `1`, and one `2`.

They are arranged in the required order.

---

## Approach

We can solve this problem using the **Dutch National Flag Algorithm**.

We use three pointers:

```text
low
mid
high
```

They divide the array into four sections:

```text
0s        1s          unknown          2s
↓         ↓              ↓              ↓
[ 0 0 | 1 1 |   ? ? ?   | 2 2 ]
       low  mid          high
```

The goal is to move:

- All `0`s to the left.
- All `1`s to the middle.
- All `2`s to the right.

---

## Three Pointers

### `low`

Points to the position where the next `0` should be placed.

### `mid`

Points to the current element that we are checking.

### `high`

Points to the position where the next `2` should be placed.

---

## Rules

While `mid <= high`:

### If `nums[mid] == 0`

Move `0` to the beginning.

```text
swap(nums[low], nums[mid])
```

Then:

```text
low += 1
mid += 1
```

---

### If `nums[mid] == 1`

`1` is already in the correct middle section.

So only:

```text
mid += 1
```

---

### If `nums[mid] == 2`

Move `2` to the end.

```text
swap(nums[mid], nums[high])
```

Then:

```text
high -= 1
```

We do **not** increase `mid` here because the new value that came from `high` has not been checked yet.

---

## Algorithm

1. Set `low = 0`.
2. Set `mid = 0`.
3. Set `high = len(nums) - 1`.
4. While `mid <= high`:
   - If current value is `0`, swap it with `low`.
   - If current value is `1`, move `mid`.
   - If current value is `2`, swap it with `high`.
5. Continue until all elements are processed.
6. The array will be sorted as `0, 1, 2`.

---

## Dry Run

Consider:

```text
nums = [2,0,2,1,1,0]
```

Initial:

```text
low = 0
mid = 0
high = 5
```

### Step 1

Current:

```text
nums[mid] = 2
```

Swap with `high`:

```text
[0,0,2,1,1,2]
```

Now:

```text
high = 4
mid = 0
```

---

### Step 2

Current:

```text
nums[mid] = 0
```

Swap with `low`:

```text
[0,0,2,1,1,2]
```

Move:

```text
low = 1
mid = 1
```

---

### Step 3

Current:

```text
nums[mid] = 0
```

Swap with `low`:

```text
[0,0,2,1,1,2]
```

Move:

```text
low = 2
mid = 2
```

---

### Step 4

Current:

```text
nums[mid] = 2
```

Swap with `high`:

```text
[0,0,1,1,2,2]
```

Move:

```text
high = 3
```

`mid` stays at `2`.

---

### Step 5

Current:

```text
nums[mid] = 1
```

`1` is already in the correct section.

```text
mid = 3
```

---

### Step 6

Current:

```text
nums[mid] = 1
```

Again:

```text
mid = 4
```

Now:

```text
mid > high
```

The process stops.

Final array:

```text
[0,0,1,1,2,2]
```

---

## Solution

```python id="j7x2mc"
class Solution:
    def sortColors(self, nums):
        low = 0
        mid = 0
        high = len(nums) - 1

        while mid <= high:

            # 0 should go to the beginning
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1

            # 1 stays in the middle
            elif nums[mid] == 1:
                mid += 1

            # 2 should go to the end
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
```

---

## How the Code Works

### 1. Initialize three pointers

```python id="u4v9pk"
low = 0
mid = 0
high = len(nums) - 1
```

Initially:

```text
low  → beginning
mid  → beginning
high → end
```

---

### 2. Process the array

```python id="r2m6xz"
while mid <= high:
```

We continue until the unknown section becomes empty.

---

### 3. When the value is `0`

```python id="f7q3mn"
if nums[mid] == 0:
    nums[low], nums[mid] = nums[mid], nums[low]
    low += 1
    mid += 1
```

`0` belongs at the beginning.

So we swap it with the element at `low`.

---

### 4. When the value is `1`

```python id="k8p4wd"
elif nums[mid] == 1:
    mid += 1
```

`1` belongs in the middle.

Therefore, no swapping is needed.

---

### 5. When the value is `2`

```python id="s5x9qa"
else:
    nums[mid], nums[high] = nums[high], nums[mid]
    high -= 1
```

`2` belongs at the end.

We swap it with the element at `high`.

Notice that `mid` does **not** increase.

This is important because the new value placed at `mid` still needs to be checked.

---

## Important Edge Cases

### Case 1: Only zeros

```text
Input:
[0,0,0]

Output:
[0,0,0]
```

---

### Case 2: Only ones

```text
Input:
[1,1,1]

Output:
[1,1,1]
```

---

### Case 3: Only twos

```text
Input:
[2,2,2]

Output:
[2,2,2]
```

---

### Case 4: Already sorted

```text
Input:
[0,1,2]

Output:
[0,1,2]
```

---

### Case 5: Reverse order

```text
Input:
[2,1,0]

Output:
[0,1,2]
```

---

### Case 6: Single element

```text
Input:
[1]

Output:
[1]
```

---

## Complexity Analysis

### Time Complexity

```text
O(n)
```

Each element is processed a constant number of times.

### Space Complexity

```text
O(1)
```

The array is modified **in-place** and only three pointers are used.

---

## Key Concept

The main concept used in this problem is the:

**Dutch National Flag Algorithm**

It divides the array into three regions:

```text
+---------+---------+-----------+---------+
|    0    |    1    |  Unknown  |    2    |
+---------+---------+-----------+---------+
     ↑         ↑          ↑           ↑
    low       mid       mid         high
```

The final arrangement is:

```text
0 0 0 0 | 1 1 1 | 2 2 2 2
```

---

## Why Not Use `sort()`?

The problem specifically says:

```text
Do not use the library's sort function.
```

Therefore, we manually rearrange the elements using swaps.

This also gives:

```text
Time  → O(n)
Space → O(1)
```

---

## Constraints

```text
n == nums.length
1 <= n <= 300
nums[i] is either 0, 1, or 2
```

---

## Language

**Python**

---

## LeetCode Information

- **Problem:** Sort Colors
- **Problem Number:** 75
- **Difficulty:** Medium
- **Topic:** Array
- **Pattern:** Two Pointers / Dutch National Flag

---

## File Structure

```text
75-sort-colors/
├── README.md
└── solution.py
```

---

## Solution Link

[View Solution](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/75-sort-colors/solution.py)

---

## Repository Link

[LeetCode_solution](https://github.com/suchita4004-collab/LeetCode_solution)
``````markdown id="a3x7kp"
# 75 - Sort Colors

## Problem

You are given an array `nums` containing objects of three colors:

- `0` → Red
- `1` → White
- `2` → Blue

Sort the array **in-place** so that the colors appear in this order:

```text
0 → 1 → 2
```

You are **not allowed to use the library's sorting function**.

The solution should modify the original array directly.

---

## Examples

### Example 1

**Input:**
```text
nums = [2,0,2,1,1,0]
```

**Output:**
```text
[0,0,1,1,2,2]
```

**Explanation:**

The array contains:

```text
0 → two times
1 → two times
2 → two times
```

After sorting:

```text
[0,0,1,1,2,2]
```

---

### Example 2

**Input:**
```text
nums = [2,0,1]
```

**Output:**
```text
[0,1,2]
```

**Explanation:**

There is one `0`, one `1`, and one `2`.

They are arranged in the required order.

---

## Approach

We can solve this problem using the **Dutch National Flag Algorithm**.

We use three pointers:

```text
low
mid
high
```

They divide the array into four sections:

```text
0s        1s          unknown          2s
↓         ↓              ↓              ↓
[ 0 0 | 1 1 |   ? ? ?   | 2 2 ]
       low  mid          high
```

The goal is to move:

- All `0`s to the left.
- All `1`s to the middle.
- All `2`s to the right.

---

## Three Pointers

### `low`

Points to the position where the next `0` should be placed.

### `mid`

Points to the current element that we are checking.

### `high`

Points to the position where the next `2` should be placed.

---

## Rules

While `mid <= high`:

### If `nums[mid] == 0`

Move `0` to the beginning.

```text
swap(nums[low], nums[mid])
```

Then:

```text
low += 1
mid += 1
```

---

### If `nums[mid] == 1`

`1` is already in the correct middle section.

So only:

```text
mid += 1
```

---

### If `nums[mid] == 2`

Move `2` to the end.

```text
swap(nums[mid], nums[high])
```

Then:

```text
high -= 1
```

We do **not** increase `mid` here because the new value that came from `high` has not been checked yet.

---

## Algorithm

1. Set `low = 0`.
2. Set `mid = 0`.
3. Set `high = len(nums) - 1`.
4. While `mid <= high`:
   - If current value is `0`, swap it with `low`.
   - If current value is `1`, move `mid`.
   - If current value is `2`, swap it with `high`.
5. Continue until all elements are processed.
6. The array will be sorted as `0, 1, 2`.

---

## Dry Run

Consider:

```text
nums = [2,0,2,1,1,0]
```

Initial:

```text
low = 0
mid = 0
high = 5
```

### Step 1

Current:

```text
nums[mid] = 2
```

Swap with `high`:

```text
[0,0,2,1,1,2]
```

Now:

```text
high = 4
mid = 0
```

---

### Step 2

Current:

```text
nums[mid] = 0
```

Swap with `low`:

```text
[0,0,2,1,1,2]
```

Move:

```text
low = 1
mid = 1
```

---

### Step 3

Current:

```text
nums[mid] = 0
```

Swap with `low`:

```text
[0,0,2,1,1,2]
```

Move:

```text
low = 2
mid = 2
```

---

### Step 4

Current:

```text
nums[mid] = 2
```

Swap with `high`:

```text
[0,0,1,1,2,2]
```

Move:

```text
high = 3
```

`mid` stays at `2`.

---

### Step 5

Current:

```text
nums[mid] = 1
```

`1` is already in the correct section.

```text
mid = 3
```

---

### Step 6

Current:

```text
nums[mid] = 1
```

Again:

```text
mid = 4
```

Now:

```text
mid > high
```

The process stops.

Final array:

```text
[0,0,1,1,2,2]
```

---

## Solution

```python id="j7x2mc"
class Solution:
    def sortColors(self, nums):
        low = 0
        mid = 0
        high = len(nums) - 1

        while mid <= high:

            # 0 should go to the beginning
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1

            # 1 stays in the middle
            elif nums[mid] == 1:
                mid += 1

            # 2 should go to the end
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
```

---

## How the Code Works

### 1. Initialize three pointers

```python id="u4v9pk"
low = 0
mid = 0
high = len(nums) - 1
```

Initially:

```text
low  → beginning
mid  → beginning
high → end
```

---

### 2. Process the array

```python id="r2m6xz"
while mid <= high:
```

We continue until the unknown section becomes empty.

---

### 3. When the value is `0`

```python id="f7q3mn"
if nums[mid] == 0:
    nums[low], nums[mid] = nums[mid], nums[low]
    low += 1
    mid += 1
```

`0` belongs at the beginning.

So we swap it with the element at `low`.

---

### 4. When the value is `1`

```python id="k8p4wd"
elif nums[mid] == 1:
    mid += 1
```

`1` belongs in the middle.

Therefore, no swapping is needed.

---

### 5. When the value is `2`

```python id="s5x9qa"
else:
    nums[mid], nums[high] = nums[high], nums[mid]
    high -= 1
```

`2` belongs at the end.

We swap it with the element at `high`.

Notice that `mid` does **not** increase.

This is important because the new value placed at `mid` still needs to be checked.

---

## Important Edge Cases

### Case 1: Only zeros

```text
Input:
[0,0,0]

Output:
[0,0,0]
```

---

### Case 2: Only ones

```text
Input:
[1,1,1]

Output:
[1,1,1]
```

---

### Case 3: Only twos

```text
Input:
[2,2,2]

Output:
[2,2,2]
```

---

### Case 4: Already sorted

```text
Input:
[0,1,2]

Output:
[0,1,2]
```

---

### Case 5: Reverse order

```text
Input:
[2,1,0]

Output:
[0,1,2]
```

---

### Case 6: Single element

```text
Input:
[1]

Output:
[1]
```

---

## Complexity Analysis

### Time Complexity

```text
O(n)
```

Each element is processed a constant number of times.

### Space Complexity

```text
O(1)
```

The array is modified **in-place** and only three pointers are used.

---

## Key Concept

The main concept used in this problem is the:

**Dutch National Flag Algorithm**

It divides the array into three regions:

```text
+---------+---------+-----------+---------+
|    0    |    1    |  Unknown  |    2    |
+---------+---------+-----------+---------+
     ↑         ↑          ↑           ↑
    low       mid       mid         high
```

The final arrangement is:

```text
0 0 0 0 | 1 1 1 | 2 2 2 2
```

---

## Why Not Use `sort()`?

The problem specifically says:

```text
Do not use the library's sort function.
```

Therefore, we manually rearrange the elements using swaps.

This also gives:

```text
Time  → O(n)
Space → O(1)
```

---

## Constraints

```text
n == nums.length
1 <= n <= 300
nums[i] is either 0, 1, or 2
```

---

## Language

**Python**

---

## LeetCode Information

- **Problem:** Sort Colors
- **Problem Number:** 75
- **Difficulty:** Medium
- **Topic:** Array
- **Pattern:** Two Pointers / Dutch National Flag

---

## File Structure

```text
75-sort-colors/
├── README.md
└── solution.py
```

---

## Solution Link

[View Solution](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/75-sort-colors/solution.py)

---

## Repository Link

[LeetCode_solution](https://github.com/suchita4004-collab/LeetCode_solution)
```
