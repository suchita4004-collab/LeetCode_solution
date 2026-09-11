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
