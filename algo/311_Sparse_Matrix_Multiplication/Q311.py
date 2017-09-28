class Solution:
    def matrixMultiply(self, A, B):
        '''
        A: int[][]
        B: int[][]
        '''
        if not A or not A[0] or not B or not B[0]:
            return None
        m, n, nb = len(A), len(A[0]), len(B[0])
        C = [[0 for _ in xrange(nb)] for _ in xrange(m)]

        for i in xrange(m):
            for k in xrange(n):
                if A[i][k] != 0:
                    for j in xrange(nb):
                        if B[k][j] != 0:
                            C[i][j] += A[i][k] * B[k][j]
        return C
