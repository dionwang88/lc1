class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        不仅要检查pattern有没有，还要检查s字符串value有没有匹配过
        """
        s = s.split()
        if len(pattern) != len(s):
            return False

        pmap = {}
        smap = {}
        for i in xrange(len(pattern)):
            if pattern[i] not in pmap:
                if s[i] not in smap:
                    pmap[pattern[i]] = s[i]
                    smap[s[i]] = pattern[i]
                else:
                    return False
            else:
                if pmap[pattern[i]] != s[i]:
                    return False
        return True
