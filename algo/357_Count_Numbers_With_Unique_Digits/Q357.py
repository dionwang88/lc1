class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        :desc: for n = 2, the unique numbers are 9 * 9, for n = 3, the unique numbers are 9 * 9 * 8
        then the formular is 9 * 9 * ... * 1
        """
        if n == 0:
            return 1
        if n == 1:
            return 9
        res = 10
        for i in xrange(2, n + 1):
            res += self.helper(i)
        return res

    def helper(self, n):
        product = 1
        for i in xrange(n):
            if i > 9:
                break
            if i == 0:
                product *= 9
            else:
                product *= (9 - i + 1)
        return product

sol = Solution()
print sol.countNumbersWithUniqueDigits(4)
