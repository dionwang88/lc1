class Solution:
    def longestValidParentheses(self, s):
        if len(s) < 2:
            return 0
        curMax = 0
        dp = [0] * len(s)
        for i in xrange(1, len(s)):
            if s[i] == ')':
                if s[i - 1] == '(':
                    dp[i] = 2 + dp[i - 2] if i - 2 >= 0 else 2
                    curMax = max(curMax, dp[i])
                else:
                    if (i - dp[i - 1] - 1) >= 0 and s[i - dp[i - 1] - 1] == '(':
                        temp = dp[i - dp[i - 1] - 2] if (i - dp[i - 1] - 2) >= 0 else 0
                        dp[i] = dp[i - 1] + 2 + temp
                        curMax = max(curMax, dp[i])
        return curMax
sol = Solution()
print sol.longestValidParentheses('(()())')
