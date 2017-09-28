class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bull, cow = 0, 0
        smap, gmap = {}, {}
        for i in xrange(len(secret)):
            if secret[i] == guess[i]:
                bull += 1
            else:
                if secret[i] in smap:
                    smap[secret[i]] += 1
                else:
                    smap[secret[i]] = 1
                if guess[i] in gmap:
                    gmap[guess[i]] += 1
                else:
                    gmap[guess[i]] = 1
        for g in gmap:
            for i in xrange(gmap[g]):
                if g in smap and smap[g] > 0:
                    cow += 1
                    smap[g] -= 1
        return str(bull) + 'A' + str(cow) + 'B'

sol = Solution()
print sol.getHint('1807', '8710')
