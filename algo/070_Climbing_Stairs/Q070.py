class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n
        ret = [0] * n
        ret[0] = 1
        ret[1] = 2
        for i in xrange(2, n):
            ret[i] = ret[i - 1] + ret[i - 2]
        return ret[n - 1]
