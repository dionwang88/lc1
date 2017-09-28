class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        A = [0] * (rowIndex + 1)
        A[0] = 1
        for i in xrange(1, rowIndex + 1):
            j = i
            while j >= 1:
                A[j] += A[j - 1]
                j -= 1
        return A

sol = Solution()
print sol.getRow(4)
