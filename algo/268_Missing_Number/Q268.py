class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        :desc: The basic idea is to use XOR operation. We all know that a^b^b =a, which means two xor operations with
        the same number will eliminate the number and reveal the original number.
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        res = 0
        for i in xrange(len(nums)):
            res = res ^ i ^ nums[i]
        return res ^ (len(nums))

sol = Solution()
print sol.missingNumber([0,1,2,3,4,6])
