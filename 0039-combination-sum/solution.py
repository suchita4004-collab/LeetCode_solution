class Solution:
    def combinationSum(self, candidates, target):
        result = []

        def backtrack(start, remaining, combination):
            if remaining == 0:
                result.append(combination.copy())
                return

            if remaining < 0:
                return

            for i in range(start, len(candidates)):
                if candidates[i] > remaining:
                    continue

                combination.append(candidates[i])

                # Use the same candidate again
                backtrack(i, remaining - candidates[i], combination)

                combination.pop()

        candidates.sort()
        backtrack(0, target, [])

        return result
