### Output

[0, 1]

### Explanation

The numbers `2` and `7` add up to the target `9`.

Therefore, the answer is `[0, 1]`.

## Approach

I use a dictionary to store each number and its index.

For each number, I calculate its complement:

`complement = target - current number`

If the complement is already in the dictionary, I return the two indices.

Otherwise, I store the current number and its index.

## Complexity

- Time Complexity: O(n)
- Space Complexity: O(n)

## Solution

[View Solution](solution.py)
