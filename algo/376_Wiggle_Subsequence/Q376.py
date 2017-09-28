class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        贪心法
        '''
        count1, count2 = 1, 1
        for i in xrange(1, len(nums)):
            if nums[i] > nums[i-1]:
                count1 = count2 + 1
            elif nums[i] < nums[i-1]:
                count2 = count1 + 1
        return len(nums) == 0 ? 0 : max(count1, count2)

    def wiggleMaxLength1(self, nums):
        '''
        Dynamic Programming
        '''
        if len(nums) == 0:
            return 0
        f = [1] * len(nums)
        d = [1] * len(nums)
        for i in xrange(1, len(nums)):
            for j in xrange(i):
                if nums[j] < nums[i]:
                    f[i] = max(f[i], d[j] + 1)
                elif nums[j] > nums[i]:
                    d[i] = max(d[i], f[j] + 1)
        return max(f[-1], d[-1])
