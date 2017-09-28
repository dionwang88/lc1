class SegmentTree:
    def __init__(self, nums):
        import sys
        self.nums = nums
        self.st = [sys.maxint] * (pow(2,len(nums) - 1) - 1)

    def buildST(self, low, high, pos):
        if low == high:
            self.st[pos] = self.nums[low]
            return
        mid = (low + high) / 2
        self.buildST(low, mid, 2 * pos + 1)
        self.buildST(mid + 1, high, 2 * pos + 2)
        self.st[pos] = min(self.st[2 * pos + 1], self.st[2 * pos + 2])

    def rangeMinimumQuery(self, qlow, qhigh, low, high, pos):
        import sys
        if qlow <= low and qhigh >= high:
            return self.st[pos]
        if qlow  > high or qhigh < low:
            return sys.maxint
        mid = (low + high) / 2
        return min(self.rangeMinimumQuery(qlow, qhigh, low, mid, 2 * pos + 1), \
                   self. rangeMinimumQuery(qlow, qhigh, mid + 1, high, 2 * pos + 2))

segmenttree = SegmentTree([-1, 2, 4, 0, 3])
segmenttree.buildST(0, len(segmenttree.nums) - 1, 0)
print segmenttree.st
print segmenttree.rangeMinimumQuery(1, 3, 0, 3, 0)
