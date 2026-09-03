# Substring with Concatenation of All Words

## Problem

Given a string `s` and an array of strings `words`, where all the words have the same length, find all starting indices of substrings in `s` that are a concatenation of every word in `words`.

The words can appear in any order, but each word must appear exactly as many times as it appears in `words`.

Return the starting indices in any order.

## Example 1

**Input**

```text
s = "barfoothefoobarman"
words = ["foo","bar"]
```

### Output

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/30-substring-with-concatenation-of-all-words/README.md#output)

```text
[0,9]
```

### Explanation

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/30-substring-with-concatenation-of-all-words/README.md#explanation)

The substring starting at index `0` is:

```text
"barfoo"
```

It is a concatenation of `"bar"` and `"foo"`.

The substring starting at index `9` is:

```text
"foobar"
```

It is also a concatenation of `"foo"` and `"bar"`.

Therefore, the answer is `[0,9]`.

## Example 2

**Input**

```text
s = "wordgoodgoodgoodbestword"
words = ["word","good","best","word"]
```

### Output

```text
[]
```

### Explanation

[svg](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/30-substring-with-concatenation-of-all-words/README.md#explanation)

There is no substring that contains all the words with the required frequencies.

Therefore, the answer is an empty array.

## Example 3

**Input**

```text
s = "barfoofoobarthefoobarman"
words = ["bar","foo","the"]
```

### Output

```text
[6,9,12]
```

### Explanation

The valid concatenated substrings are:

```text
"foobarthe"  → index 6
"barthefoo"  → index 9
"thefoobar"  → index 12
```

Therefore, the answer is `[6,9,12]`.

## Approach

I use a **sliding window** with a frequency dictionary.

First, I store the required frequency of every word in `word_freq`.

Since all words have the same length, I check the string in groups of `word_len` characters.

For each possible starting offset:

1. Take the next word from the string.
2. Check if the word exists in `word_freq`.
3. If it does not exist, reset the current window.
4. Otherwise, add the word to `current_freq`.
5. If a word appears too many times, move the left side of the window forward.
6. When the window contains exactly `word_count` words, add its starting index to the result.
7. Move the window forward and continue searching.

This allows all valid concatenations to be found without checking every permutation of the words.

## Complexity

Let `n` be the length of `s` and `m` be the total number of words.

- **Time Complexity:** O(n)
- **Space Complexity:** O(m)

The frequency dictionaries store the words and their counts.

## Solution

[View Solution](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/30-substring-with-concatenation-of-all-words/solution.py)

## Folder Structure

```text
30-substring-with-concatenation-of-all-words/
├── README.md
└── solution.py
```
