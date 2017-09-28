class Solution(object):
    def __init__(self):
        self.ret = []
# 这个超时了
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        dfs([], 1, n, k)
        return self.ret

    def dfs(self, comb, start, n, k):
        if k == 0:
            self.ret.append(list(comb))
            return
        for i in xrange(start, n + 1):
            comb.append(i)
            dfs(comb, i + 1, n, k - 1)
            comb = comb[:-1]
