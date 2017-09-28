class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        https://www.youtube.com/watch?v=WepWFGxiwRs
        动态规划的解法，该解法用了滚动数组，降低了空间复杂度
        f[j]就是从0-j这段子字符串是否是True，该解法就是从0-j进行split，
        如果有0-i(不包含i), i-j都在dictionary里面，则f[j]为True，
        如果有一部分不在dictionary里面，则f[j]为False
        具体解法思路可以看视频
        """
        f = [False] * (len(s) + 1)
        f[0] = True

        for i in xrange(len(s) + 1):
            for j in xrange(i):
                if f[j] and s[j, i] in wordDict:
                    f[i] = True
                    break
        return f[len(s)]
