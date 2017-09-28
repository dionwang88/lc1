class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mmap = {}
        for num in nums:
            if num in mmap:
                mmap[num] += 1
            else:
                mmap[num] = 1
        for num in mmap:
            if mmap[num] > len(nums) / 2:
                return num
