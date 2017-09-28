class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 0
        if n == 2:
            return 1
        if n == 3:
            return 2
        if n == 4:
            return 4
        left = n
        res = 1
        while left > 4:
            left -= 3
            res *= 3
        if left > 0:
            res *= left
        return res
