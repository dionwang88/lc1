class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 0:
            return ''

        nmap = {}
        res = ''
        for i in xrange(1, 27):
            nmap[i] = chr(ord('A') + i - 1)
        while n > 0:
            r = n % 26
            if r == 0:
                r = 26
            temp = nmap[r]
            res = temp + res
            n /= 26
            if r == 26:
                n -= 1
        return res

sol = Solution()
print sol.convertToTitle(26)
