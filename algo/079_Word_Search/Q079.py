class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        对每一个位置的字符都从四个方向进行深度优先搜索
        注意当有一个字符匹配时占位的方式,退出时要重新把字符重置
        """
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if self.dfs(board, i, j, word, 0):
                    return True
        return False

    def dfs(self, board, i, j, word, ind):
        if ind == len(word):
            return True
        if i > len(board) - 1 or i < 0 or j < 0 or j > len(board[0]) - 1 or board[i][j] != word[ind]:
            return False
        board[i][j] = '*'
        result = self.dfs(board, i - 1, j, word, ind + 1) or \
                 self.dfs(board, i, j - 1, word, ind + 1) or \
                 self.dfs(board, i + 1, j, word, ind + 1) or \
                 self.dfs(board, i, j + 1, word, ind + 1)
        board[i][j] = word[ind]
        return result

sol = Solution()
board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
print sol.exist(board, 'SEE')
