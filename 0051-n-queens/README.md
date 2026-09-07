# 0051 - N-Queens

## Problem

The **N-Queens** puzzle asks us to place `n` queens on an `n x n` chessboard such that no two queens can attack each other.

Given an integer `n`, return all distinct solutions.

A queen can attack another queen if they are in the same:

- Row
- Column
- Diagonal

Each solution is represented as a list of strings where:

- `Q` represents a queen.
- `.` represents an empty space.

## Example 1

Input:

```text
n = 4
