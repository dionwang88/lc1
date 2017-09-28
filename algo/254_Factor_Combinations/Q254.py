
class Solution:
    def __init__(self):
        self.res = []

    def getFactors(self, n):
        '''
        The logic is in here:
        http://www.cnblogs.com/airwindow/p/4822572.html
        This has optimization method
        https://segmentfault.com/a/1190000005801106
        :param n:
        :return:
        '''
        self.helper([], n, 2)
        return self.res

    def helper(self, path, n, start):
        if n == 1:
            if len(path) > 1:
                self.res.append(path)
            return
        for i in xrange(start, int(math.sqrt(n)) + 1):
            if n % i == 0:
                self.helper(path + [i], n / i, i)
                path = path[:-1]
        self.helper(path + [n], 1, n) # be careful here should add n again

sol = Solution()
print sol.getFactors(12)
