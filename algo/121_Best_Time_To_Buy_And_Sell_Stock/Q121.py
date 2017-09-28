class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        import sys
        minV, res = sys.maxint, 0
        for i in prices:
            minV = min(minV, i)
            res = max(res, i - minV)
        return res

sol = Solution()
print sol.maxProfit([7,2,5,3,1,6])
