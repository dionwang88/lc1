class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], res)
        return res


    def dfs (self, nums, target, index, path, res) :
        '''
        DFS基本都是这个模式套路，要熟练掌握
        '''
        if target == 0:
            res.append(path)
            return
        if target < 0:
            return
        for i in xrange(index, len(nums)):
            if nums[i] > target:  #here
                break
            self.dfs(nums, target-nums[i], i, path+[nums[i]], res)
