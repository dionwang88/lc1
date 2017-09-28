class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        这个题目没通过，应该是不明白数独的规则
        """
        if len(board) < 1 or len(board[0]) < 1:
            return False
        for i in xrange(len(board)):
            smap = {'.': 1}
            for j in xrange(len(board[0])):
                c = board[i][j]
                if c == '.':
                    continue
                elif int(c) > 0 and int(c) < 10 and c not in smap:
                    smap[c] = 1
                else:
                    return False
        for j in xrange(len(board[0])):
            smap = {'.': 1}
            for i in xrange(len(board)):
                c = board[i][j]
                if c == '.':
                    continue
                elif int(c) > 0 and int(c) < 10 and c not in smap:
                    smap[c] = 1
                else:
                    return False
        return True

sol = Solution()
print sol.isValidSudoku(["....5..1.",".4.3.....",".....3..1","8......2.","..2.7....",".15......",".....2...",".2.9.....","..4......"])
