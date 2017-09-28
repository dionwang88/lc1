class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        smap, tmap = {}, {}
        for ss in s:
            if ss in smap:
                smap[ss] += 1
            else:
                smap[ss] = 1
        for tt in t:
            if tt in tmap:
                tmap[tt] += 1
            else:
                tmap[tt] = 1
        for ss in smap:
            for i in xrange(smap[ss]):
                if ss in tmap:
                    if tmap[ss] > 0:
                        tmap[ss] -= 1
                    else:
                        return False
                else:
                    return False
        return True
