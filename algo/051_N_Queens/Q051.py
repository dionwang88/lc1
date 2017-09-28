class Solution:
    '''
    这个问题转换成一个一位数组，查看 p + q == x + y or p - q == x - y
    In this problem, whenever a location (x, y) is occupied, any other locations
    (p, q ) where p + q == x + y or p - q == x - y would be invalid. We can use
    this information to keep track of the indicators (xy_dif and xy_sum ) of the
    invalid positions and then call DFS recursively with valid positions only.
    '''
    def solveNQueens(self, n):
        def DFS(queens, xy_dif, xy_sum):
            p = len(queens)
            if p == n:
                result.append(queens)
                return None
            for q in range(n):
                if q not in queens and p - q not in xy_dif and p + q not in xy_sum:
                    DFS(queens + [q], xy_dif + [p - q], xy_sum + [p + q])
        result = []
        DFS([], [], [])
        return [["." * i + "Q" + "." * (n - i - 1) for i in sol] for sol in result]

sol = Solution()
sol.solveNQueens(5)
