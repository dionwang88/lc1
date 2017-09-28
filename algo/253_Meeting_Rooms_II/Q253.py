import Queue as Q

class Solution:
    def canAttendMeeting(self, intervals):
        if not intervals or len(intervals) == 0:
            return 0
        intervals.sort()
        endTimes = Q.PriorityQueue()
        endTimes.put(intervals[0][1])
        for interval in intervals:
            endTime = endtimes.get()
            if interval[0] < endTime: # if current start time less than min end time, then push back the original end time and add a new room
                endTimes.put(endTime)
            endTimes.put(interval[1])
        return endTimes.qsize()
