class Solution:
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 3:
            return False
        import sys
        small = big = sys.maxint
        for n in nums:
            if n <= small:
                small = n
            elif n <= big:
                big = n
            else:
                return True
        return False

sol = Solution()
print sol.increasingTriplet([5,1,5,5,3, 2, 5,4])
