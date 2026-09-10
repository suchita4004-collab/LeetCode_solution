```python
class Solution:
    def isNumber(self, s):
        i = 0
        n = len(s)

        # Check optional sign
        if i < n and (s[i] == '+' or s[i] == '-'):
            i += 1

        digits_before = 0
        digits_after = 0

        # Check digits before decimal point
        while i < n and s[i].isdigit():
            digits_before += 1
            i += 1

        # Check decimal point and digits after it
        if i < n and s[i] == '.':
            i += 1

            while i < n and s[i].isdigit():
                digits_after += 1
                i += 1

        # A decimal/integer must contain at least one digit
        if digits_before == 0 and digits_after == 0:
            return False

        # Check exponent
        if i < n and (s[i] == 'e' or s[i] == 'E'):
            i += 1

            # Exponent can have an optional sign
            if i < n and (s[i] == '+' or s[i] == '-'):
                i += 1

            exponent_digits = 0

            while i < n and s[i].isdigit():
                exponent_digits += 1
                i += 1

            # Exponent must contain at least one digit
            if exponent_digits == 0:
                return False

        # Entire string must be processed
        return i == n
```
