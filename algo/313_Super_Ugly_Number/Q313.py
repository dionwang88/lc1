import sys

class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        http://www.cnblogs.com/Liok3187/p/5016076.html
        """
        ugly = [0] * n
        idx = [0] * len(primes)

        ugly[0] = 1
        for i in xrange(1, n):
            # find next
            ugly[i] = sys.maxint
            for j in xrange(len(primes)):
                val = primes[j] * ugly[idx[j]]
                if ugly[i] > val:
                    ugly[i] = val
            # # slip duplicate
            for j in xrange(len(primes)):
                while primes[j] * ugly[idx[j]] <= ugly[i]:
                    idx[j] += 1
        return ugly[n - 1]

    def nthSuperUglyNumber1(self, n, primes):
        ugly = [0] * n
        ugly[0] = 1
        ugly_idx = 1
        idx = [0] * len(primes)
        while ugly_idx <= n:
            # find next
            minVal = ugly[ugly_idx] = sys.maxint
            prime_idx = 0
            for j in xrange(len(primes)):
                val = primes[j] * ugly[idx[j]]
                if ugly[ugly_idx] > val:
                    ugly[ugly_idx] = val
                    minVal = val
                    prime_idx = j
            # If there is duplicated then slip duplicate
            # avoid loop the prime array, just do the same index of the ugly array again
            if minVal != ugly[ugly_idx - 1]:
                ugly[ugly_idx] = minVal
                ugly_idx += 1

        return ugly[n - 1]

sol = Solution()
print sol.nthSuperUglyNumber(8, [2, 5, 7])
