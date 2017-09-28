class Solution(object):
    def __init__(self):
        self.ret = False
        self.smap = {}

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        self.helper(n)
        return self.ret


    def helper(self, m):
        if m == 1:
            self.ret = True
            return
        if m in self.smap:
            self.ret = False
            return
        self.smap[m] = 1
        total = 0
        for i in str(m):
            total += int(i) * int(i)
        self.helper(total)

sol = Solution()
print sol.isHappy(1111111)
