class Solution:
    def getPermutation(self, n, k):
        numbers = [str(i) for i in range(1, n + 1)]

        factorial = 1
        for i in range(1, n):
            factorial *= i

        k -= 1
        result = ""

        while numbers:
            index = k // factorial
            result += numbers.pop(index)

            if not numbers:
                break

            k %= factorial
            factorial //= len(numbers)

        return result
