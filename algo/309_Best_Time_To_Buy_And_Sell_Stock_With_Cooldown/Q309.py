class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        https://discuss.leetcode.com/topic/30421/share-my-thinking-process
        buy[i]  = max(rest[i-1]-price, buy[i-1])  这一次买，或者是上一次买
        sell[i] = max(buy[i-1]+price, sell[i-1])  这一次卖，或者是上一次卖
        rest[i] = max(sell[i-1], buy[i-1], rest[i-1]) 这一次休息，或者上一次休息
        buy[i] <= rest[i] <= sell[i]  ==> rest[i] = sel[i - 1]
        Then:
        buy[i] = max(sell[i - 1] - price, buy[i - 1])
        sell[i] = max(buy[i - 1] + price, sell[i - 1])
        """
        buy, sell = -sys.maxint, 0
        prev_buy, prev_sell = 0, 0
        for price in prices:
            prev_buy = buy
            buy = max(prev_sell - price, prev_buy)
            prev_sell = sell
            sell = max(prev_buy + price, prev_sell)
        return sell
