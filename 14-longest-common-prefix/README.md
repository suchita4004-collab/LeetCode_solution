# Longest Common Prefix

## Problem

You are given an array of strings `strs`.

Find the longest common prefix string among all the strings.

If there is no common prefix, return an empty string `""`.

### Example 1

**Input**

```text id="w1k4jd"
strs = ["flower","flow","flight"]
```

### Output

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/14-longest-common-prefix/README.md#output)

"fl"

### Explanation

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/14-longest-common-prefix/README.md#explanation)

The strings `"flower"`, `"flow"`, and `"flight"` all start with `"fl"`.

Therefore, the longest common prefix is `"fl"`.

### Example 2

**Input**

```text id="p5k8sc"
strs = ["dog","racecar","car"]
```

### Output

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/14-longest-common-prefix/README.md#output)

""

### Explanation

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/14-longest-common-prefix/README.md#explanation)

The strings `"dog"`, `"racecar"`, and `"car"` do not have any common starting characters.

Therefore, the answer is an empty string `""`.

## Approach

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/14-longest-common-prefix/README.md#approach)

I take the first string as the initial prefix.

Then, I compare it with each of the remaining strings.

If a string does not start with the current prefix, I remove the last character from the prefix.

I continue removing characters until the current string starts with the prefix.

If the prefix becomes empty, I return `""`.

After checking all the strings, the remaining prefix is the longest common prefix.

## Complexity

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/14-longest-common-prefix/README.md#complexity)

* Time Complexity: O(n × m)
* Space Complexity: O(1)

Where `n` is the number of strings and `m` is the length of the shortest string.

## Solution

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/14-longest-common-prefix/README.md#solution)

[View Solution](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/14-longest-common-prefix/solution.py)
