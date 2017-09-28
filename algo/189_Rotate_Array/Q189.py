class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        遇到循环数组的情况，通常要考虑翻转
        """
        if k == 0 or len(nums) == 0 or k % len(nums) == 0:
            return
        k = k % len(nums)
        self.reverse(nums, 0, len(nums) - 1)
        print nums
        self.reverse(nums, 0, k - 1)
        print nums
        self.reverse(nums, k, len(nums) - 1)
        print nums

    def reverse(self, nums, start, end):
        while start < end:
            temp = nums[start]
            nums[start] = nums[end]
            nums[end] = temp
            start += 1
            end -= 1

sol = Solution()
sol.rotate([1,2,3,4,5,6,7], 8)
