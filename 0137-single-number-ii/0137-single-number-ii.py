class Solution:
    def singleNumber(self, nums):
        result = 0

        for i in range(32):
            count = 0

            for num in nums:
                if (num >> i) & 1:
                    count += 1

            if count % 3 != 0:
                result |= (1 << i)

        # Handle negative numbers
        if result >= 2**31:
            result -= 2**32

        return result