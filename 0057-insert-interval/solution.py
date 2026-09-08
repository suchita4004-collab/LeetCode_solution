class Solution:
    def insert(self, intervals, newInterval):
        result = []

        start, end = newInterval

        for s, e in intervals:

            # Current interval is completely before newInterval
            if e < start:
                result.append([s, e])

            # Current interval is completely after newInterval
            elif s > end:
                result.append([start, end])
                start, end = s, e

            # Current interval overlaps with newInterval
            else:
                start = min(start, s)
                end = max(end, e)

        # Add the final new/merged interval
        result.append([start, end])

        return result
