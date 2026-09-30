class Solution:
    def maxDepthAfterSplit(self, seq):
        answer = []
        depth = 0

        for ch in seq:
            if ch == '(':
                depth += 1
                answer.append(depth % 2)
            else:
                answer.append(depth % 2)
                depth -= 1

        return answer