# Largest Rectangle in Histogram

## Problem

You are given an array `heights` representing the heights of bars in a histogram.

- Each bar has a width of `1`.
- We need to find the **largest rectangle** that can be formed inside the histogram.
- Return the area of the largest rectangle.

### Example 1

**Input:**
```text
heights = [2,1,5,6,2,3]
```

**Output:**
```text
10
```

The largest rectangle is formed using the bars with heights `5` and `6`.

The minimum height is `5` and the width is `2`.

```text
Area = height × width
     = 5 × 2
     = 10
```

### Example 2

**Input:**
```text
heights = [2,4]
```

**Output:**
```text
4
```

---

## Approach

We use a **Monotonic Increasing Stack**.

The stack stores the indexes of bars in increasing order of height.

When we find a bar that is smaller than the bar at the top of the stack, we know that the taller bar cannot extend any further to the right.

So, we remove it from the stack and calculate the rectangle area.

### Main Idea

For every bar, we need to know:

- The first smaller bar on the left.
- The first smaller bar on the right.

These boundaries tell us how wide the rectangle can be.

The stack helps us find these boundaries efficiently.

---

## Why Use a Stack?

A simple solution would check every possible rectangle, but that can take `O(n²)` time.

The stack allows us to process every bar only a small number of times.

Therefore:

```text
Time Complexity = O(n)
Space Complexity = O(n)
```

---

## Algorithm

1. Create an empty stack.
2. Add a `0` at the end of `heights`.
   - This forces all remaining bars in the stack to be processed.
3. Traverse the histogram from left to right.
4. If the current bar is taller than or equal to the stack top:
   - Push its index into the stack.
5. If the current bar is shorter than the stack top:
   - Remove the taller bar.
   - Calculate its possible rectangle width.
   - Calculate its area.
   - Update the maximum area.
6. Continue until all bars are processed.
7. Remove the extra `0`.
8. Return the maximum area.

---

## Dry Run

Consider:

```text
heights = [2,1,5,6,2,3]
```

We add `0`:

```text
[2,1,5,6,2,3,0]
```

### Process 2

Stack:

```text
[2]
```

### Process 1

`1` is smaller than `2`.

Remove `2`.

Width:

```text
1
```

Area:

```text
2 × 1 = 2
```

Maximum:

```text
2
```

Stack:

```text
[1]
```

### Process 5

Stack:

```text
[1,5]
```

### Process 6

Stack:

```text
[1,5,6]
```

### Process 2

`2` is smaller than `6`.

Remove `6`.

```text
Area = 6 × 1 = 6
```

Now `2` is also smaller than `5`.

Remove `5`.

The width is:

```text
2
```

Area:

```text
5 × 2 = 10
```

Maximum:

```text
10
```

### Process 3

Stack continues with the appropriate indexes.

### Process 0

The final `0` removes the remaining bars and checks their possible rectangles.

The largest area remains:

```text
10
```

Therefore:

```text
Output = 10
```

---

## Understanding the Width

Suppose we remove a bar at index `i`.

The current index is the first smaller bar on the right.

The new stack top is the first smaller bar on the left.

Therefore:

```text
width = right - left - 1
```

In the code:

```python
width = i - stack[-1] - 1
```

If there is no smaller bar on the left:

```python
width = i
```

---

## Important Trick: Add 0 at the End

We add:

```python
heights.append(0)
```

Why?

Consider:

```text
[2,4,5]
```

The bars are increasing, so they would remain in the stack.

The extra `0` is smaller than all of them:

```text
[2,4,5,0]
```

This forces the stack to process all remaining bars.

After processing, we remove it:

```python
heights.pop()
```

---

## How the Code Works

### Create Stack

```python
stack = []
max_area = 0
```

The stack stores indexes of bars.

### Add Zero

```python
heights.append(0)
```

This makes sure all remaining bars are processed.

### Traverse the Histogram

```python
for i, height in enumerate(heights):
```

We check every bar from left to right.

### Remove Taller Bars

```python
while stack and heights[stack[-1]] > height:
```

If the current bar is shorter, the taller bar can no longer extend to the right.

### Calculate Height

```python
h = heights[stack.pop()]
```

The removed bar becomes the height of the rectangle.

### Calculate Width

```python
if stack:
    width = i - stack[-1] - 1
else:
    width = i
```

This determines how many bars can be included in the rectangle.

### Calculate Area

```python
area = h * width
max_area = max(max_area, area)
```

We calculate the rectangle area and keep the largest value.

---

## Visual Understanding

For:

```text
[2,1,5,6,2,3]
```

The important rectangle is:

```text
      5   6
      █   █
      █   █
      █   █
      █   █
      █   █
```

The rectangle uses two bars:

```text
Height = 5
Width  = 2
```

Therefore:

```text
Area = 5 × 2 = 10
```

---

## Important Edge Cases

### 1. Single Bar

```text
Input: [5]
Output: 5
```

### 2. Increasing Heights

```text
Input: [1,2,3,4,5]
Output: 9
```

The best rectangle has height `3` and width `3`.

```text
3 × 3 = 9
```

### 3. Decreasing Heights

```text
Input: [5,4,3,2,1]
Output: 9
```

### 4. All Bars Have Same Height

```text
Input: [2,2,2,2]
Output: 8
```

```text
Area = 2 × 4 = 8
```

### 5. Zero Height

```text
Input: [0,2,0]
Output: 2
```

The zero-height bars separate the histogram.

---

## Complexity Analysis

Let `n` be the number of bars.

### Time Complexity

```text
O(n)
```

Each bar is pushed into and removed from the stack at most once.

### Space Complexity

```text
O(n)
```

In the worst case, the stack can contain all the indexes.

---

## Key Concept

The main concept used in this problem is:

**Monotonic Increasing Stack**

The stack maintains indexes of bars in increasing order of height.

When a smaller bar is found, we calculate the maximum rectangle that can be formed using the taller bars.

---

## Constraints

- `1 <= heights.length <= 10^5`
- `0 <= heights[i] <= 10^4`

Because `n` can be as large as `100,000`, an `O(n²)` solution would be too slow.

The `O(n)` stack solution is efficient enough.

---

## Language

**Python**

---

## LeetCode Information

- **Problem Number:** 84
- **Problem Name:** Largest Rectangle in Histogram
- **Difficulty:** Hard
- **Topic:** Array, Stack, Monotonic Stack

---

## File Structure

```text
LeetCode_solution/
│
└── 84-largest-rectangle-in-histogram/
    ├── README.md
    └── solution.py
```

---

## Solution Link

[View Solution](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/84-largest-rectangle-in-histogram/solution.py)

## Repository Link

[LeetCode_solution](https://github.com/suchita4004-collab/LeetCode_solution)
