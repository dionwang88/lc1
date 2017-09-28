class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        :desc: if current greater than previous then add the difference of current to previous
        """
        if not prices:
            return 0
        res = 0
        for i in xrange(1, len(prices)):
            res += prices[i] - prices[i - 1] if prices[i] - prices[i - 1] > 0 else 0
        return res

sol = Solution()
print sol.maxProfit([2,-1,3,4,8,0,6])
