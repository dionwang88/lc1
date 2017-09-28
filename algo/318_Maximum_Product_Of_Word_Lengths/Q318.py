class Solution(object):
    def maxProduct(self, words):
        '''
        注意这个位操作是如何判断两个字符串有相同字符的:
        value[i] |= 1 << (ord(w) - ord('a'))
        判断value[i] & value[j] == 0
        :param words:
        :return:
        '''
        if len(words) < 2:
            return 0
        value = [0] * len(words)
        for i in xrange(len(words)):
            for w in words[i]:
                value[i] |= 1 << (ord(w) - ord('a'))
        maxProduct = 0
        for i in xrange(len(words)):
            for j in xrange(i + 1, len(words)):
                if (value[i] & value[j] == 0):
                    maxProduct = max(maxProduct, len(words[i]) * len(words[j]))
        return maxProduct

sol = Solution()
print sol.maxProduct(['abcd', 'ertrt', 'lkj'])
