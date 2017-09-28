class Solution(object):
    def __init__(self):
        self.nums = []

    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 1
        self.nums = nums
        k = self.partition()
        index = k
        for i in xrange(k):
            temp = abs(self.nums[i])
            if temp <= k:
                self.nums[temp - 1] = self.nums[temp - 1] if self.nums[temp - 1] < 0 else -self.nums[temp - 1]
        for i in xrange(len(self.nums)):
            if self.nums[i] > 0:
                index = i
                break
        return index + 1

    def partition(self):
        i, j = 0, 0
        for k in xrange(len(self.nums)):
            if self.nums[j] > 0:
                self.swap(i, j)
                i += 1
                j += 1
            else:
                j += 1
        return i

    def swap(self, i, j):
        temp = self.nums[i]
        self.nums[i] = self.nums[j]
        self.nums[j] = temp

nums = [2, 3, -1, 0]
s = Solution()
print s.firstMissingPositive(nums)
