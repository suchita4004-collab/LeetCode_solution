# 0057 - Insert Interval

## Problem

You are given an array of non-overlapping intervals `intervals`, where:

```text
intervals[i] = [starti, endi]
```

The intervals are already sorted in ascending order according to their starting values.

You are also given another interval:

```text
newInterval = [start, end]
```

The task is to insert `newInterval` into `intervals` such that:

- The intervals remain sorted.
- There are no overlapping intervals.
- Overlapping intervals are merged.

The problem does not require modifying the original array in-place.

## Examples

### Example 1

Input:

```text
intervals = [[1,3],[6,9]]
newInterval = [2,5]
```

Output:

```text
[[1,5],[6,9]]
```

Explanation:

`[1,3]` overlaps with `[2,5]`, so they are merged:

```text
[1,3] + [2,5] = [1,5]
```

Final result:

```text
[[1,5],[6,9]]
```

### Example 2

Input:

```text
intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
```

Output:

```text
[[1,2],[3,10],[12,16]]
```

Explanation:

`[4,8]` overlaps with:

```text
[3,5]
[6,7]
[8,10]
```

All of these intervals are merged:

```text
[3,5] + [4,8] + [6,7] + [8,10]
= [3,10]
```

Therefore:

```text
[[1,2],[3,10],[12,16]]
```

## Approach

Since the input intervals are already sorted, we can solve the problem in one traversal without sorting them again.

There are three possible cases for every interval.

### Case 1: Interval is before the new interval

If:

```text
end < new_start
```

there is no overlap.

So, add the current interval directly to the result.

Example:

```text
Current:    [1,2]
New:              [4,8]
```

Since:

```text
2 < 4
```

we add `[1,2]`.

### Case 2: Interval is after the new interval

If:

```text
start > new_end
```

the current interval comes completely after the new interval.

Before adding it, we first add the new interval to the result.

Example:

```text
Current:             [10,12]
New:        [4,8]
```

Since:

```text
10 > 8
```

we add `[4,8]` first and then continue with `[10,12]`.

### Case 3: Intervals overlap

Otherwise, the current interval overlaps with the new interval.

We merge them using:

```python
start = min(start, s)
end = max(end, e)
```

For example:

```text
New interval:     [4,8]
Current:          [6,10]
```

After merging:

```text
[4,10]
```

## Algorithm

1. Create an empty `result` list.
2. Store the start and end of `newInterval`.
3. Traverse every interval.
4. If the interval is completely before `newInterval`, add it to `result`.
5. If the interval is completely after `newInterval`:
   - Add the current merged `newInterval`.
   - Make the current interval the new interval.
6. Otherwise, merge the current interval with `newInterval`.
7. After the loop, add the final merged interval.
8. Return `result`.

## Solution

```python
class Solution:
    def insert(self, intervals, newInterval):
        result = []

        start, end = newInterval

        for s, e in intervals:

            # Current interval is completely before newInterval
            if e < start:
                result.append([s, e])

            # Current interval is completely after newInterval
            elif s > end:
                result.append([start, end])
                start, end = s, e

            # Current interval overlaps with newInterval
            else:
                start = min(start, s)
                end = max(end, e)

        # Add the final new/merged interval
        result.append([start, end])

        return result
```

## Dry Run

Consider:

```text
intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
```

### Step 1

Current interval:

```text
[1,2]
```

Since:

```text
2 < 4
```

it is before the new interval.

```text
result = [[1,2]]
```

### Step 2

Current interval:

```text
[3,5]
```

It overlaps with `[4,8]`.

Merge:

```text
start = min(4,3) = 3
end = max(8,5) = 8
```

New merged interval:

```text
[3,8]
```

### Step 3

Current interval:

```text
[6,7]
```

It overlaps.

Merged interval remains:

```text
[3,8]
```

### Step 4

Current interval:

```text
[8,10]
```

It overlaps because the intervals share the point `8`.

Merge:

```text
[3,10]
```

### Step 5

Current interval:

```text
[12,16]
```

Since:

```text
12 > 10
```

it is after the merged interval.

Add:

```text
[3,10]
```

Then process `[12,16]`.

Finally:

```text
result = [[1,2],[3,10],[12,16]]
```

## Complexity

Let `n` be the number of intervals.

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)`

We traverse the intervals only once. The output array may contain up to `n + 1` intervals.

## Key Concept

The main idea is to divide the intervals into three categories:

```text
1. Before newInterval
2. Overlapping with newInterval
3. After newInterval
```

The overlap condition can be handled by checking whether the current interval is neither completely before nor completely after the new interval.

Important conditions:

```python
if e < start:
```

means the interval is before the new interval.

```python
elif s > end:
```

means the interval is after the new interval.

Otherwise, the intervals overlap and must be merged.

## Constraints

- `0 <= intervals.length <= 10^4`
- `intervals[i].length == 2`
- `0 <= starti <= endi <= 10^5`
- `intervals` is sorted by starting value in ascending order.
- `newInterval.length == 2`
- `0 <= start <= end <= 10^5`

## Language

Python

## LeetCode Problem

**Problem Number:** 57

**Problem Name:** Insert Interval

**Difficulty:** Medium

## Solution Link

[View Solution on GitHub](solution.py)

## Problem Link

[LeetCode – Insert Interval](https://leetcode.com/problems/insert-interval/)
