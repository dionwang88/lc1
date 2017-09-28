class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        ret = [0] * (num + 1)
        if num == 0:
            return ret
        ret[1] = 1
        if num == 1:
            return ret
        i, index = 2, 2
        while i < num + 1:
            start, end = pow(2, index - 1), pow(2, index)
            theRange = end - start
            mid = start + theRange / 2
            j = start - theRange / 2
            while i < num + 1 and i < mid:
                ret[i] = ret[j]
                i += 1
                j += 1
            j = start
            while i < num + 1 and i >= mid and i < end:
                ret[i] = ret[j] + 1
                j += 1
                i += 1
            index += 1
        return ret

sol = Solution()
print sol.countBits(31)
