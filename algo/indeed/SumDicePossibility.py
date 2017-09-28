class SumPossibility:
    def __init__(self):
        self.count = 0

    def sumPossibilityBF(self, n, target):
        if n <= 0 or target <= 0:
            return 0

        self.helper(n, target, 0)
        return self.count

    def helper(self, n, target, a):
        if n == 1:
            for i in xrange(1, 7):
                if a + i == target:
                    self.count += 1
            return

        for j in xrange(1, 7):
            self.helper(n - 1, target, a + j)

    def sumPossibilityDP(self, n, target):
        if n <= 0 or target <= 0:
            return 0

        dp = [[0 for i in xrange(target + 1)] for j in xrange(n + 1)]
        dp[0][0] = 1
        for i in xrange(1, n + 1):
            for j in xrange(1, target + 1):
                for k in xrange(1, 7):
                    if j >= k:
                        dp[i][j] = dp[i][j] + dp[i - 1][j - k]
        return dp[n][target]


sp = SumPossibility()
print sp.sumPossibilityDP(4, 6)
