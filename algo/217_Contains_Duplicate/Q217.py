class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        cmap = {}
        for num in nums:
            if num in cmap:
                return True
            else:
                cmap[num] = 1
        return False
