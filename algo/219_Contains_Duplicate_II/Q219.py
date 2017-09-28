class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums) < 2:
            return False
        cmap = {}
        for i in xrange(len(nums)):
            if nums[i] in cmap:
                if i - cmap[nums[i]]<= k:
                    return True
                else:
                    cmap[nums[i]] = i
            else:
                cmap[nums[i]] = i
        return False

sol = Solution()
print sol.containsNearbyDuplicate([1,2,1], 0)
