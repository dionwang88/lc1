class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        smap = {}
        for i in xrange(len(s)):
            if s[i] in smap:
                smap[s[i]] += 1
            else:
                smap[s[i]] = 1
        for i in xrange(len(s)):
            if smap[s[i]] == 1:
                return i
        return -1
