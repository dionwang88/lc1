class Solution(object):
    '''
    还是使用上题中得dfs算法
    只是需要修改
    首先在递归调用的时候 index要每次+1 因为一个数只能用一次
    一个是要跳过一些相等的变量
    为了增加速度 可以设置当找到一个组合的时候 或者已经溢出的时候  跳出当前的循环
    因为数组是排列过的
    同时也可以跳过一些相等的变量加速
    '''
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        def dfs(target, beg, ares, candidates):
            if target == 0:
                result.append(ares)
                return
            for i in xrange(beg, len(candidates)):
                if candidates[i] > target: break
                if i-1 >= beg and candidates[i] == candidates[i-1]: continue
                dfs(target - candidates[i], i+1, ares + [candidates[i]], candidates)
        candidates.sort()
        dfs(target, 0, [], candidates)
        return result
