class Solution:
    def minCost(self, costs):
        '''
        用dp即可 每个房子只可能有三个颜色 就是三个状态 0, 1, 2
        如果是0 那么前一个房子只可能是1,2
        如果是1 那么前一个房子只可能是0,2
        如果是2 那么前一个房子只可能是0,1
        所以每个dp保存当前房子3种颜色的分别最小的cost即可
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + costs[i][0]
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + costs[i][1]
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + costs[i][2]
        costs: int[][]
        return: int
        '''
        if not costs or not costs[0]:
            return 0
        n = len(costs)
        for i in xrange(n):
            costs[i][0] = costs[i][0] + min(costs[i - 1][1], costs[i - 1][2])
            costs[i][1] = costs[i][1] + min(costs[i - 1][0], costs[i - 1][2])
            costs[i][2] = costs[i][2] + min(costs[i - 1][0], costs[i - 1][1])

        return min(costs[n - 1][0], min(costs[n - 1][1], costs[n - 1][2]))
