class Solution:
    def maxEnemyKilled(self, grid):
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        res = 0
        for i in xrange(m):
            for j in xrange(n):
                count = 0
                if grid[i][j] == 0:
                    k = j
                    while k - 1 > 0 or grid[i][k] != 'W':
                        k -= 1
                        count = self.getCount(grid, i, k, count)
                    k = j
                    while k + 1 < n or grid[i][k] != 'W':
                        k += 1
                        count = self.getCount(grid, i, k, count)
                    k = i
                    while k - 1 > 0 or grid[k][j] != 'W':
                        k -= 1
                        count = self.getCount(grid, i, k, count)
                    k = i
                    while k + 1 < m or grid[k][j] != 'W':
                        k += 1
                        count = self.getCount(grid, i, k, count)
                res = max(res, count)
        return res

    def getCount(self, grid, i, j, count):
        if grid[i][k] == 'E':
            count += 1
        return count

    def maxKilledEnemies(self, grid):
        '''
        http://www.cnblogs.com/grandyang/p/5599289.html
        '''
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        res, rowCnt, colCnt = 0, 0, [0] * n
        for i in xrange(m):
            for j in xrange(n):
                if j == 0 or grid[i][j - 1] == 'W':
                    rowCnt = 0
                    k = j
                    while k < n and grid[i][k] != 'W':
                        rowCnt = rowCnt + 1 if grid[i][k] == 'E' else rowCnt
                        k += 1
                if i == 0 or grid[i - 1][j] == 'W':
                    colCnt[j] = 0
                    k = i
                    while k < m and grid[k][j] != 'W':
                        colCnt[j] = colCnt[j] + 1 if grid[k][j] == 'E' else colCnt[j]
                        k += 1
                if grid[i][j] == '0':
                    res = max(res, rowCnt + colCnt[j])
        return res
