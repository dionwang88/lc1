class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        ret = ''
        factorial = [0] * (n + 1)
        numbers = [0] * n
        sumFact = 1
        factorial[0] = sumFact
        for i in xrange(1, n + 1):
            sumFact *= i
            factorial[i] = sumFact

        for i in xrange(1, n + 1):
            numbers[i - 1] = i

        k -= 1

        for i in xrange(1, n + 1):
            index = k / factorial[n - i]
            ret += str(numbers[index])
            del numbers[index]
            k = k % factorial[n - i]

        return ret

sol = Solution()
print sol.getPermutation(8, 5449)
