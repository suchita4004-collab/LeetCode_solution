# Integer to Roman

## Problem

You are given an integer `num`. Convert it into a Roman numeral.

Roman numerals use the following symbols:

* `I = 1`
* `V = 5`
* `X = 10`
* `L = 50`
* `C = 100`
* `D = 500`
* `M = 1000`

The subtractive forms `IV`, `IX`, `XL`, `XC`, `CD`, and `CM` are used when required.

### Example 1

**Input**

```text
num = 3749
```

### Output

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/12-integer-to-roman/README.md#output)

"MMMDCCXLIX"

### Explanation

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/12-integer-to-roman/README.md#explanation)

The number `3749` is converted based on its place values.

```text
3000 = MMM
 700 = DCC
  40 = XL
   9 = IX
```

Therefore, the Roman numeral is:

`MMMDCCXLIX`

### Example 2

**Input**

```text
num = 58
```

### Output

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/12-integer-to-roman/README.md#output)

"LVIII"

### Explanation

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/12-integer-to-roman/README.md#explanation)

```text
50 = L
 8 = VIII
```

Therefore, the answer is `LVIII`.

### Example 3

**Input**

```text
num = 1994
```

### Output

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/12-integer-to-roman/README.md#output)

"MCMXCIV"

### Explanation

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/12-integer-to-roman/README.md#explanation)

```text
1000 = M
 900 = CM
  90 = XC
   4 = IV
```

Therefore, the answer is `MCMXCIV`.

## Approach

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/12-integer-to-roman/README.md#approach)

I store the Roman numeral values and symbols in descending order.

For each value, I check if the given number is greater than or equal to that value.

If it is, I add the corresponding Roman symbol to the result and subtract its value from the number.

I continue this process until the number becomes `0`.

The subtractive forms like `CM`, `XC`, and `IV` are also included in the list, so they are handled automatically.

## Complexity

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/12-integer-to-roman/README.md#complexity)

* Time Complexity: O(n)
* Space Complexity: O(1)

## Solution

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/12-integer-to-roman/README.md#solution)

[View Solution](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/12-integer-to-roman/solution.py)
