class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        ret = [[1], [1, 1]]
        last = ret[1]

        for i in xrange(2, numRows):
            temp = [1] * (i + 1)
            for j in xrange(1, len(temp) - 1):
                temp[j] = last[j - 1] + last[j]
            last = temp
            ret.append(temp)
        return ret

sol = Solution()
print sol.generate(8)
