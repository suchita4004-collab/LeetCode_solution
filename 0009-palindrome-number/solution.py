class Solution:
    def isPalindrome(self, x):
        # Negative numbers are not palindromes
        if x < 0:
            return False

        # Numbers ending in 0 cannot be palindromes
        # unless the number itself is 0
        if x != 0 and x % 10 == 0:
            return False

        reversed_num = 0

        # Reverse only half of the number
        while x > reversed_num:
            digit = x % 10
            reversed_num = reversed_num * 10 + digit
            x //= 10

        # Even number of digits:
        # x == reversed_num
        #
        # Odd number of digits:
        # x == reversed_num // 10
        return x == reversed_num or x == reversed_num // 10
