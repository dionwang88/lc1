class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [0] * m
        dp[0] = 1
        for i in xrange(n):
            for j in xrange(1, m):
                dp[j] = dp[j - 1] + dp[j]
        return dp[m - 1]
