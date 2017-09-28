class Solution:
    def __init__(self, n):
        self.N = n
        self.rows = [0] * n
        self.cols = [0] * n
        self.diag = 0
        self.rev_diag = 0

    def move(self, row, col, player):
        '''
        我们建立一个大小为n的一维数组rows和cols，还有变量对角线diag和逆对角线rev_diag，
        这种方法的思路是，如果玩家1在第一行某一列放了一个子，那么rows[0]自增1，如果玩家2
        在第一行某一列放了一个子，则rows[0]自减1，那么只有当rows[0]等于n或者-n的时候，
        表示第一行的子都是一个玩家放的，则游戏结束返回该玩家即可，其他各行各列，对角线和
        逆对角线都是这种思路
        '''
        add = 1 if player == 1 else -1
        self.rows[row] += add
        self.cols[col] += add
        self.diag += add if row == col else 0
        self.rev_diag += add if row == (N - col - 1) else 0
        return player if (abs(rows[row] == N) or abs(cols[col] == N) or abs(diag) == N or abs(rev_diag) == N) else 0
