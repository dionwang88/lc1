class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        low, high = 0, len(nums) - 1
        while low < high:
            mid = low + (high - low) / 2
            if nums[mid] >= target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
        if low == high and low == 0:
            if nums[low] < target:
                return low + 1
            else:
                return low
        if low == high:
            if nums[low] >= target:
                return low
            else:
                return low + 1
        elif low > high:
            return low

        return -1

sol = Solution()
print sol.searchInsert([1,3], 2)
