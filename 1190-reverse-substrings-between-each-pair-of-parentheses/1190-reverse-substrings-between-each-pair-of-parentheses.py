class Solution:
    def reverseParentheses(self, s):
        stack = []

        for ch in s:
            if ch == '(':
                stack.append([])
            elif ch == ')':
                text = stack.pop()
                text.reverse()

                if stack:
                    stack[-1].extend(text)
                else:
                    stack.append(text)
            else:
                if stack:
                    stack[-1].append(ch)
                else:
                    stack.append([ch])

        return "".join(stack[0])
        