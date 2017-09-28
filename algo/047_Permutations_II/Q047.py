class Solution:
    def permuteUnique(self, nums):
        res, alist, used = [], [], [False] * len(nums)
        if not nums or len(nums) == 0:
            return res
        nums.sort()
        self.dfs(nums, used, alist, res)
        return res

    def dfs(self, nums, used, alist, res):
        if len(alist) == len(nums):
            res.append(list(alist))
            return
        for i in xrange(len(nums)):
            if used[i]:
                continue
            if i > 0 and nums[i - 1] == nums[i] and not used[i - 1]:
                continue
            used[i] = True
            alist.append(nums[i])
            self.dfs(nums, used, alist, res)
            used[i] = False
            del alist[-1]

sol = Solution()
ret = sol.permuteUnique([1, 1, 2, 2])
print ret
