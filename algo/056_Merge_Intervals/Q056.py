class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __cmp__(self, other):
        return cmp(self.start, other.start)

class Solution:
    def merge(self, intervals):
        if len(intervals) <= 1:
            return intervals

        intervals.sort()
        result = []
        start = intervals[0].start
        end = intervals[0].end
        for inte in intervals:
            if inte.start <= end:
                end = max(end, inte.end)
            else:
                result.append(Interval(start, end))
                start = inte.start
                end = inte.end
        result.append(Interval(start, end))
        return result

i1 = Interval(1, 2)
i2 = Interval(2, 4)
sol = Solution()
ret = sol.merge([i1, i2])
for interval in ret:
    print interval.start, interval.end
