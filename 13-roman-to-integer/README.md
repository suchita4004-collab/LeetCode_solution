# Roman to Integer

## Problem

You are given a string `s` containing a Roman numeral. Convert the Roman numeral into an integer.

Roman numerals use the following symbols:

```text
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
```

Roman numerals are usually written from largest to smallest. However, subtraction is used in cases such as `IV`, `IX`, `XL`, `XC`, `CD`, and `CM`.

### Example 1

**Input**

```text
s = "III"
```

### Output

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/13-roman-to-integer/README.md#output)

3

### Explanation

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/13-roman-to-integer/README.md#explanation)

`III = 1 + 1 + 1 = 3`

Therefore, the answer is `3`.

### Example 2

**Input**

```text
s = "LVIII"
```

### Output

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/13-roman-to-integer/README.md#output)

58

### Explanation

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/13-roman-to-integer/README.md#explanation)

`L = 50`, `V = 5`, and `III = 3`.

Therefore:

`50 + 5 + 3 = 58`

### Example 3

**Input**

```text
s = "MCMXCIV"
```

### Output

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/13-roman-to-integer/README.md#output)

1994

### Explanation

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/13-roman-to-integer/README.md#explanation)

The Roman numeral can be divided into:

```text
M = 1000
CM = 900
XC = 90
IV = 4
```

Therefore:

`1000 + 900 + 90 + 4 = 1994`

## Approach

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/13-roman-to-integer/README.md#approach)

I use a dictionary to store the value of each Roman numeral symbol.

I check each symbol with the symbol next to it.

If the current symbol has a smaller value than the next symbol, I subtract its value.

Otherwise, I add its value to the result.

For example, in `IV`, the value of `I` is smaller than `V`, so I subtract `1` from the result.

This handles all the subtractive cases such as `IV`, `IX`, `XL`, `XC`, `CD`, and `CM`.

## Complexity

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/13-roman-to-integer/README.md#complexity)

* Time Complexity: O(n)
* Space Complexity: O(1)

## Solution

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/13-roman-to-integer/README.md#solution)

[View Solution](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/13-roman-to-integer/solution.py)
