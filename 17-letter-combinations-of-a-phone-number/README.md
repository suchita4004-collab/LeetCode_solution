# Letter Combinations of a Phone Number

## Problem

You are given a string `digits` containing digits from `2` to `9`.

Each digit represents a group of letters like the buttons on a telephone keypad.

Return all possible letter combinations that the digits could represent.

If the input is empty, return an empty list.

### Example 1

**Input**

```text id="xw2y8c"
digits = "23"
```

### Output

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/17-letter-combinations-of-a-phone-number/README.md#output)

```text id="z8v1qu"
["ad","ae","af","bd","be","bf","cd","ce","cf"]
```

### Explanation

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/17-letter-combinations-of-a-phone-number/README.md#explanation)

The digit `2` represents `abc` and the digit `3` represents `def`.

We combine every letter from `2` with every letter from `3`.

Therefore, the possible combinations are:

`ad, ae, af, bd, be, bf, cd, ce, cf`

### Example 2

**Input**

```text id="q2e4vk"
digits = "2"
```

### Output

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/17-letter-combinations-of-a-phone-number/README.md#output)

```text id="h8y1p4"
["a","b","c"]
```

### Explanation

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/17-letter-combinations-of-a-phone-number/README.md#explanation)

The digit `2` represents the letters `a`, `b`, and `c`.

Therefore, the answer is:

`["a","b","c"]`

## Approach

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/17-letter-combinations-of-a-phone-number/README.md#approach)

I use backtracking to generate all possible combinations.

First, I store the letters corresponding to each digit in a dictionary.

Then, I select one letter from the current digit and move to the next digit.

When all digits are processed, I add the current combination to the result.

The process continues until all possible combinations are generated.

## Complexity

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/17-letter-combinations-of-a-phone-number/README.md#complexity)

* Time Complexity: O(4^n × n)
* Space Complexity: O(4^n × n)

Here, `n` is the number of digits. Each digit can represent at most 4 letters.

## Solution

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/17-letter-combinations-of-a-phone-number/README.md#solution)

[View Solution](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/17-letter-combinations-of-a-phone-number/solution.py)
