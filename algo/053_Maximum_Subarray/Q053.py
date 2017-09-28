class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        如果当前的sum小于零，则重置
        """
        if nums == None or len(nums) == 0:
            return 0

        maxVal, currentSum = nums[0], nums[0]
        for i in xrange(1, len(nums)):
            if currentSum <= 0:
                currentSum = nums[i]
            else:
                currentSum += nums[i]
            maxVal = max(maxVal, currentSum)
        return maxVal
