class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = 0
        for i in xrange(len(s) - 1, -1, -1):
            total += pow(26, (len(s) - i - 1)) * (ord(s[i]) - ord('A') + 1)
        return total
