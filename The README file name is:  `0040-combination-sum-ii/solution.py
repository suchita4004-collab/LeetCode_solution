class Solution:
    def combinationSum2(self, candidates, target):
        result = []
        candidates.sort()

        def backtrack(start, remaining, combination):
            if remaining == 0:
                result.append(combination.copy())
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                if candidates[i] > remaining:
                    break

                combination.append(candidates[i])

                backtrack(i + 1, remaining - candidates[i], combination)

                combination.pop()

        backtrack(0, target, [])

        return result
