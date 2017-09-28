class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return len(nums)
        count = 1
        i, j = 0, 1
        while j < len(nums):
            while j < len(nums) and nums[i] == nums[j]:
                j += 1
            if j < len(nums):
                i += 1
                count += 1
                nums[i] = nums[j]

        return count

sol = Solution()
print sol.removeDuplicates([1,1,2,2,3])
