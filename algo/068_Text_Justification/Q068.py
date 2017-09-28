class Solution(object):
    # 调了一个小时真不容易
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        if not words or maxWidth == 0:
            return words
        sumLen = 0
        ret, cur = [], []
        for word in words:
            sumLen += len(word)
            if sumLen + len(cur) <= maxWidth:
                cur.append(word)
            else:
                sumLen -= len(word)
                spaceNum, residuale = 0, 0
                if len(cur) > 1:
                    spaceNum = (maxWidth - sumLen) / (len(cur) - 1)
                    residuale = (maxWidth - sumLen) % (len(cur) - 1)
                for r in xrange(residuale):
                    ss = cur[r] + " "
                    cur[r] = ss
                s = (" " * spaceNum).join(cur)
                if len(s) < maxWidth:
                    s += " " * (maxWidth - len(s))
                cur = [word]
                sumLen = len(word)
                ret.append(s)
        if len(cur) > 0:
            s = " ".join(cur)
            if len(s) < maxWidth:
                s += " " * (maxWidth - len(s))
            ret.append(s)
        return ret

sol = Solution()
print sol.fullJustify([""], 2)
