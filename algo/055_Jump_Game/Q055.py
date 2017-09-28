class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if nums == None or len(nums) == 0:
            return False
        if len(nums) == 1:
            return True
        fur_pos = nums[0]
        i = 1
        while i <= fur_pos:
            if fur_pos >= len(nums) - 1:
                return True
            cur_fur_pos = i + nums[i]
            print cur_fur_pos
            if cur_fur_pos > fur_pos:
                fur_pos = cur_fur_pos
            i += 1

        return False

sol = Solution()
a = [1,2,3]
print sol.canJump(a)
