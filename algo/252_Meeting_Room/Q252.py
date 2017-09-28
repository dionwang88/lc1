class Solution:
    def meetingRoom(self, intervals):
        if len(intervals) < 2:
            return True
        intervals = sorted(intervals)
        for i in xrange(1, len(intervals)):
            pre = intervals[i - 1]
            cur = intervals[i]
            if cur[0] < pre[1]:
                return False
        return True
sol = Solution()
print sol.meetingRoom([[0, 10],[25, 10],[15, 20]])
