class Solution:
    def minCost(self, costs):
        '''
        这道题关键的地方在于 其实根据上一座房子来计算当前的房子的cost的时候 只需要上一座房子的
        最小的cost和第二小的cost
        原因是 如果不考虑各个房子要不同颜色 每座房子都选最小的cost就行了 那么现在需要不同颜色了
        如果两个临近的房子撞色了  那么就可以参考第二小的cost就行
        所以代码里使用了reduce来处理 然后前一座cost只存的有最小的那个 还有第二小的
        注意一下index 最小的cost的那个位置其实存的是第二小的cost 剩下的位置就都是最小的cost
        这样在和当前的房子进行合并计算的时候就不会出错 直接计算最小值即可
        dp[currentHouse][currentColor] = (currentColor == prevMinColor? prevSecondMin: prevMin) + costs[currentHouse][currentColor].
        '''
        import sys
        if not costs or not costs[0]:
            return 0
        n, k = len(costs), len(costs[0])
        if k == 1:
            return costs[0][0] if n == 1 else -1
        prevMin, prevMinInd, prevSecMin = 0, -1, 0 # prevSecMin always >= prevMin
        for i in xrange(n):
            minTemp, minInd, secMin = sys.maxint, -1, sys.maxint
            for j in xrange(k):
                val = costs[i][j] + (prevSecMin if j == prevMinInd else prevMin)
                if minInd < 0:      # 第一次初始化
                    minTemp = val
                    minInd = j
                elif val < minTemp: # 找到本轮的最小值
                    secMin = minTemp
                    minTemp = val
                    minInd = j
                elif val < secMin: # 找到本轮的次小值
                    secMin = val
            prevMin = minTemp    # 本轮最小值成为上一轮的最小值
            prevMinInd = minInd  # 本轮最小值的color
            prevSecMin = secMin  # 本轮次小值成为上一轮的次小值

        return prevMin

    def minCostII(self, costs):
        '''
        注意这个reduce实现的方式非常巧妙，每一次迭代首先找出当前轮次的最小值和该最小值的index，
        然后把该index值设置为该轮次的次小值，把其他部分都设置为当前轮次的最小值。
        这样在下一次迭代时，就不用判断当前最小值的color是否与上一个house的color相同了，因为
        相同color的上一次是次小值
        '''
        return min(reduce(lambda x, y: self.combine(y, x), costs)) if costs else 0

    def combine(self, house, tmp):
        m, n, i = min(tmp), len(tmp), tmp.index(min(tmp))
        tmp = [m]*i + [min(tmp[0:i]+tmp[i+1:])] + [m]*(n-i-1)
        return [sum(i) for i in zip(house, tmp)]
