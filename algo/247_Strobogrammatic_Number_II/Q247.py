class Solution:
    def getStrobogrammatic(self, length):
        return self.helper(length, length)

    def helper(self, n, m):
        if n == 0:
            return ['']
        if n == 1:
            return ['0', '1', '8']
        l = self.helper(n - 2, m)
        res = []
        for i in xrange(len(l)):
            if n != m:
                res.append('0' + l[i] + '0')
            res.append('1' + l[i] + '1')
            res.append('6' + l[i] + '9')
            res.append('8' + l[i] + '8')
            res.append('9' + l[i] + '6')
        return res

sol = Solution()
print sol.getStrobogrammatic(5)
