class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == "0" or num2 == "0":
            return "0"

        m, n = len(num1), len(num2)
        pos = [0] * (m + n)
        for i in xrange(m - 1, -1, -1):
            for j in xrange(n - 1, -1, -1):
                mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                p1, p2 = i + j, i + j + 1
                s = mul + pos[p2]

                pos[p1] += s / 10
                pos[p2] = s % 10
        ret = ''
        for i in pos:
            if not (ret == '' and i == 0):
                ret += str(i)
        return ret

s = Solution()
print s.multiply('1', '6')
