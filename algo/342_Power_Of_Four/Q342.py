class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if (num <= 0):
            return False;
        if (num & num - 1):
            return False;
        return num % 3 == 1;
