class Solution:
    def myAtoi(self, s):
        INT_MIN = -2147483648
        INT_MAX = 2147483647

        i = 0
        n = len(s)

        # 1. Skip leading spaces
        while i < n and s[i] == ' ':
            i += 1

        # 2. Check sign
        sign = 1

        if i < n and s[i] == '-':
            sign = -1
            i += 1
        elif i < n and s[i] == '+':
            i += 1

        # 3. Read digits
        number = 0

        while i < n and '0' <= s[i] <= '9':
            digit = ord(s[i]) - ord('0')

            number = number * 10 + digit

            # 4. Check overflow
            if sign == 1 and number > INT_MAX:
                return INT_MAX

            if sign == -1 and number > 2147483648:
                return INT_MIN

            i += 1

        return sign * number
