class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        Power of 2 means only one bit of n is '1', so use the trick n&(n-1)==0
        to judge whether that is the case
        """
        if (n <= 0):
            return False
        return not (n & (n - 1))
