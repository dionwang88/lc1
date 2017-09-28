class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if matrix == None or len(matrix) == 0 or matrix[0] == None or len(matrix[0]) == 0:
            return
        middle, row, col = (len(matrix) - 1) / 2, 0, len(matrix) - 1
        while row <= middle:
            j = row
            for i in xrange(row, col - j):
                temp1 = matrix[j][i]
                temp2 = matrix[i][col - j]
                temp3 = matrix[col - j][col - i]
                temp4 = matrix[col - i][j]

                matrix[i][col-j] = temp1;
                matrix[col-j][col-i] = temp2;
                matrix[col-i][j] = temp3;
                matrix[j][i] = temp4;
            row += 1
