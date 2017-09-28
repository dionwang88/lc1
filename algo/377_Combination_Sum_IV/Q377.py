'''
这个题用了DP的思想，借鉴了Q070
注意一开始先把数组排序
以目标值为循环的退出条件，每一次遍历的值产生可能的排列都是前面左右的可能性之和
'''
class Solution(object):
    def combinationSum4(self, nums, target):
        nums.sort()
        res = [0] * (target + 1)
        for i in xrange(1, target + 1):
            for num in nums:
                if num > i:
                    break
                elif num == i:
                    res[i] += 1
                else:
                    res[i] += res[i - num]
        return res[target]

sol = Solution()
for i in xrange(1, 10):
    print sol.combinationSum4([1,2,3], i)
