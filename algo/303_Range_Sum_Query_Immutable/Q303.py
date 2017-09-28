class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.nums = [0] * len(nums)
        if len(nums) > 0:
            self.nums[0] = nums[0]
            for i in xrange(1, len(nums)):
                self.nums[i] = self.nums[i - 1] + nums[i]

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        if len(self.nums) == 0:
            return 0
        if i == 0:
            return self.nums[j]
        return self.nums[j] - self.nums[i - 1]

# Your NumArray object will be instantiated and called as such:
nums = [-2, 0, 3, -5, 2, -1]
numArray = NumArray(nums)
print numArray.sumRange(0, 2)
print numArray.sumRange(2, 5)
print numArray.sumRange(0, 5)
