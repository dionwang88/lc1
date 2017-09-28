class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        smap, tmap = {}, {}
        for i in xrange(len(s)):
            if s[i] in smap:
                if smap[s[i]] != t[i]:
                    return False
            else:
                if t[i] not in tmap:
                    smap[s[i]] = t[i]
                    tmap[t[i]] = s[i]
                else:
                    return False
        return True
