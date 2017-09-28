'''
Given a m x n grid filled with non-negative numbers, find a path from top left
to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
'''
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        Using DP
        """
        m, n = len(grid), len(grid[0])
        for i in xrange(m):
            for j in xrange(n):
                if (i == 0 and j != 0):
                    grid[i][j] += grid[i][j - 1]
                if (i != 0 and j == 0):
                    grid[i][j] += grid[i - 1][j]
                if (i != 0 and j != 0):
                    grid[i][j] += min(grid[i-1][j], grid[i][j - 1])
        return grid[m - 1][n - 1]
