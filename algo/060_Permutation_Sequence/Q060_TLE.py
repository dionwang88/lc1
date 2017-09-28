class Solution(object):
    def __init__(self):
        self.k = 0
        '''
        这种方法超时了，让求第k个，没必要把所有的排列都求出来
        '''
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        nums = []
        for i in xrange(1, n + 1):
            nums.append(i)
        res = []
        self.dfs(nums, [], res, k)
        s = ''
        for i in res[k - 1]:
            s += str(i)
        return s

    def dfs(self, nums, path, res, k):
        if not nums:
            self.k += 1
            res.append(path)
        for i in xrange(len(nums)):
            if self.k == k:
                break
            self.dfs(nums[:i] + nums[i + 1:], path + [nums[i]], res, k)

sol = Solution()
print sol.getPermutation(9, 54494)
