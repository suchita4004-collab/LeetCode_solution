```markdown
# 71 - Simplify Path

## Problem

You are given an absolute path for a Unix-style file system.

The path always starts with `/`.

Your task is to convert the given path into its **simplified canonical path**.

The rules are:

- `.` represents the current directory.
- `..` represents the parent directory.
- Multiple `/` are treated as a single `/`.
- Names such as `...` and `....` are valid directory names.
- The final path must start with exactly one `/`.
- Directories must be separated by exactly one `/`.
- The final path should not end with `/`, except for the root directory.

---

## Examples

### Example 1

**Input:**
```text
path = "/home/"
```

**Output:**
```text
/home
```

**Explanation:**

The trailing `/` is removed.

---

### Example 2

**Input:**
```text
path = "/home//foo/"
```

**Output:**
```text
/home/foo
```

**Explanation:**

Multiple consecutive slashes are treated as one slash.

---

### Example 3

**Input:**
```text
path = "/home/user/Documents/../Pictures"
```

**Output:**
```text
/home/user/Pictures
```

**Explanation:**

`..` means go to the parent directory.

So:

```text
/home/user/Documents/../Pictures
```

becomes:

```text
/home/user/Pictures
```

---

### Example 4

**Input:**
```text
path = "/../"
```

**Output:**
```text
/
```

**Explanation:**

We cannot go above the root directory.

Therefore, the result remains `/`.

---

### Example 5

**Input:**
```text
path = "/.../a/../b/c/../d/./"
```

**Output:**
```text
/.../b/d
```

**Explanation:**

`...` is a valid directory name.

- `...` → valid directory
- `a` → add directory
- `..` → remove `a`
- `b` → add directory
- `c` → add directory
- `..` → remove `c`
- `d` → add directory
- `.` → ignore

Final path:

```text
/.../b/d
```

---

## Approach

We can solve this problem using a **Stack**.

The stack stores the valid directories in the current path.

For every part of the path:

- If it is empty → ignore it.
- If it is `.` → ignore it.
- If it is `..` → remove the last directory from the stack.
- Otherwise → add the directory to the stack.

Finally, join all directories with `/`.

---

## Why Use a Stack?

A stack follows **Last In, First Out (LIFO)**.

When we see:

```text
/home/user/Documents/..
```

The `..` means we need to remove the most recently added directory:

```text
Documents
```

So the stack is perfect for this problem.

Example:

```text
Stack:
[home, user, Documents]

After "..":

[home, user]
```

---

## Algorithm

1. Create an empty stack.
2. Split the path using `/`.
3. Traverse every part.
4. If the part is empty or `.`, ignore it.
5. If the part is `..`:
   - If the stack is not empty, remove the last directory.
   - If the stack is empty, do nothing.
6. Otherwise, add the directory name to the stack.
7. Join the stack elements using `/`.
8. Add `/` at the beginning.
9. Return the simplified path.

---

## Dry Run

Consider:

```text
path = "/home/user/Documents/../Pictures"
```

After splitting:

```text
["", "home", "user", "Documents", "..", "Pictures"]
```

Process each part:

| Part | Action | Stack |
|------|--------|-------|
| `""` | Ignore | `[]` |
| `home` | Add | `[home]` |
| `user` | Add | `[home, user]` |
| `Documents` | Add | `[home, user, Documents]` |
| `..` | Remove last | `[home, user]` |
| `Pictures` | Add | `[home, user, Pictures]` |

Final stack:

```text
[home, user, Pictures]
```

Join the elements:

```text
/home/user/Pictures
```

Therefore:

```text
Output = "/home/user/Pictures"
```

---

## Solution

```python
class Solution:
    def simplifyPath(self, path):
        stack = []

        # Split the path using "/"
        parts = path.split("/")

        for part in parts:
            # Ignore empty parts and current directory "."
            if part == "" or part == ".":
                continue

            # Go to parent directory
            if part == "..":
                if stack:
                    stack.pop()

            # Valid directory/file name
            else:
                stack.append(part)

        # Build the canonical path
        return "/" + "/".join(stack)
```

---

## How the Code Works

### 1. Create a stack

```python
stack = []
```

The stack stores valid directory names.

---

### 2. Split the path

```python
parts = path.split("/")
```

For example:

```text
/home//foo/
```

becomes:

```text
["", "home", "", "foo", ""]
```

---

### 3. Ignore empty parts and `.`

```python
if part == "" or part == ".":
    continue
```

Empty parts occur because of `/` or multiple consecutive slashes.

The `.` represents the current directory, so it does not change the path.

---

### 4. Handle `..`

```python
if part == "..":
    if stack:
        stack.pop()
```

`..` means move to the parent directory.

So we remove the last directory from the stack.

If the stack is empty, we are already at the root and cannot move further up.

---

### 5. Add valid directory names

```python
else:
    stack.append(part)
```

Any other name is a valid directory or file name.

For example:

```text
...
....
home
user
```

are all treated as normal names.

---

### 6. Create the final path

```python
return "/" + "/".join(stack)
```

If:

```text
stack = ["home", "user", "Pictures"]
```

then:

```text
"/" + "home/user/Pictures"
```

gives:

```text
/home/user/Pictures
```

If the stack is empty:

```text
"/" + ""
```

gives:

```text
/
```

---

## Important Edge Cases

### Case 1: Multiple slashes

```text
Input:  "/home//foo///bar"
Output: "/home/foo/bar"
```

Empty parts are ignored.

---

### Case 2: Current directory

```text
Input:  "/home/./user"
Output: "/home/user"
```

`.` is ignored.

---

### Case 3: Parent directory

```text
Input:  "/home/user/../"
Output: "/home"
```

`user` is removed.

---

### Case 4: Going above root

```text
Input:  "/../../"
Output: "/"
```

The stack is empty, so `..` has no effect.

---

### Case 5: Valid names containing multiple periods

```text
Input: "/.../...."
Output: "/.../...."
```

Only `.` and `..` have special meanings.

`...` and `....` are normal directory names.

---

## Complexity Analysis

### Time Complexity

```text
O(n)
```

We process every character/part of the path approximately once.

### Space Complexity

```text
O(n)
```

The stack can contain directory names from the entire path.

Where `n` is the length of the input path.

---

## Key Concept

The main concept used in this problem is:

**Stack**

The stack helps us easily move back to the previous directory when we encounter `..`.

### Important Rules

```text
"."   → Ignore
".."  → Pop from stack
"abc" → Push into stack
"//"  → Treat as "/"
```

---

## Constraints

```text
1 <= path.length <= 3000
```

The path consists of:

- English letters
- Digits
- `.`
- `/`
- `_`

The given path is always a valid absolute Unix path.

---

## Language

**Python**

---

## LeetCode Information

- **Problem:** Simplify Path
- **Problem Number:** 71
- **Difficulty:** Medium
- **Topic:** Stack
- **Pattern:** Path Simplification

---

## File Structure

```text
71-simplify-path/
├── README.md
└── solution.py
```

---

## Solution Link

[View Solution](https://github.com/suchita4004-collab/LeetCode_solution/blob/main/71-simplify-path/solution.py)

---

## Repository Link

[LeetCode_solution](https://github.com/suchita4004-collab/LeetCode_solution)
```
