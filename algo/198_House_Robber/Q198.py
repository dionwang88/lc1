class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a, b = 0, 0
        for i in xrange(len(nums)):
            if i % 2 == 0:
                a = max(a + nums[i], b)
            else:
                b = max(a, b + nums[i])
        return max(a, b)
