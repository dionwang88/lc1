class Solution(object):
    def __init__(self):
        self.res = []

    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        if k == 0:
            return self.res

        chars = [i for i in xrange(1, 10)]
        self.dfs(chars, 1, [], k, n)
        return self.res

    def dfs(self, chars, start, path, k, n):
        if k == 0 and n == 0:
            self.res.append(path)
        if k > 0 and n > 0:
            for i in xrange(start, len(chars) + 1):
                self.dfs(chars, i + 1, path + [i], k - 1, n - i)
        else:
            return

sol = Solution()
print sol.combinationSum3(3, 9)
