class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        :type size: int
        """
        self.nums = nums
        self.amap = {}
        for i in xrange(len(nums)):
            self.amap[i] = nums[i]

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        for key in self.amap:
            self.nums[key] = self.amap[key]
        return self.nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        from random import random

        if not self.nums:
            return None
        for j in xrange(1, len(self.nums)):
            i = int(random() * (j + 1))
            self.swap(i, j)
        return self.nums

    def swap(self, i, j):
        temp = self.nums[i]
        self.nums[i] = self.nums[j]
        self.nums[j] = temp

sol = Solution([4,7,9])
print sol.shuffle()
print sol.reset()