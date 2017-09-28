class Solution:
    def paintFence(self, n, k):
        if n < 2:
            return n * k
        diff = k * (k - 1)
        same = k
        for i in xrange(2, n):
            temp = diff
            diff = (diff + same) * (k - 1)
            same = temp
        return diff + same
