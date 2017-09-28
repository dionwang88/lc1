class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        buf = []
        s = s.lower()
        for ss in s:
            if (ord(ss) >= ord('a') and ord(ss) <= ord('z')) or (ord(ss) >= ord('0') and ord(ss) <= ord('9')):
                buf.append(ss)
        i, j = 0, len(buf) - 1
        while i < j:
            if buf[i] != buf[j]:
                return False
            i += 1
            j -= 1
        return True
sol = Solution()
print sol.isPalindrome("0P")
