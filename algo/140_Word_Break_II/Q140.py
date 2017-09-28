class Solution(object):
    def __init__(self):
        self.map = {}

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        if s in self.map:
            return self.map[s]
        res = []
        if len(s) == 0:
            res.append('')
            return res
        for word in wordDict:
            if word == s[0:len(word)]:
                sublist = self.wordBreak(s[len(word):], wordDict)
                for sub in sublist:
                    space = ''
                    if len(sub) > 0:
                        space = ' '
                    res.append(word + space + sub)
        self.map[s] = res
        return res

sol = Solution()
print sol.wordBreak("catsanddog", ["cat","cats","and","sand","dog"])
