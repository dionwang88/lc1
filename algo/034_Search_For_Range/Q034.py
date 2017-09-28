class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = [-1, -1]
        if not nums:
            return ret

        l, r = 0, len(nums) - 1
        while(l < r):
            mid = (l + r) / 2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        if nums[l] != target:
            return res
        else:
            res[0] = l

        r = len(nums) - 1
        while(l < r):
            mid = (l + r) / 2 + 1
            if nums[mid] > target:
                r = mid - 1
            else:
                l = mid
        res[1] = r

        return res
