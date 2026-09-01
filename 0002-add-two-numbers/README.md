# 2. Add Two Numbers

**Difficulty:** Medium  
**Language:** Python

## Problem

Given two non-empty linked lists representing two non-negative integers, add the two numbers and return the result as a linked list.

The digits are stored in reverse order.

## Example

### Input

l1 = [2,4,3]  
l2 = [5,6,4]

### Output

[7,0,8]

### Explanation

The linked lists represent:

342 + 465 = 807

Therefore, the result is:

[7,0,8]

## Approach

I traverse both linked lists at the same time.

For each pair of nodes, I add their values along with the carry from the previous calculation.

The current digit is calculated using:

digit = total % 10

The carry is calculated using:

carry = total // 10

I continue until both lists are completely traversed and there is no remaining carry.

## Complexity

- Time Complexity: O(max(n, m))
- Space Complexity: O(max(n, m))

## Solution

[View Solution](solution.py)
