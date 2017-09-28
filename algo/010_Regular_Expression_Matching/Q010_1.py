// Recursion Solution

class Solution:
    def isMatch(self, s, p):
        if not p:
            return not s

        if p[-1] == '*':
            if s and (s[-1] == p[-2] or p[-2] == '.'):
                return self.isMatch(s, p[:-2]) or self.isMatch(s[:-1], p)
            else:
                return self.isMatch(s, p[:-2])
        else:
            if s and (s[-1] == p[-1] or p[-1] == '.'):
                return self.isMatch(s[:-1], p[:-1])
            else:
                return False
