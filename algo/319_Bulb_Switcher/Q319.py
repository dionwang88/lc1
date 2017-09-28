import math
class Solution(object):
    def bulbSwitch(self, n):
        if n < 2:
            return 0
        if n < 4:
            return 2
        for i in xrange(4, n + 1):
            ret = [True] * i
            for j in xrange(2, i):
                for k in xrange(j - 1, i, j):
                    ret[k] = not ret[k]
            print i, sum(ret), ret

    def bulbSwitch1(self, n):
        return int(math.sqrt(n))


sol = Solution()
print sol.bulbSwitch1(25)
