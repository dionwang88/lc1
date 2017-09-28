class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3:
            return len(nums)

        wMap = {}
        count = 0
        for num in nums:
            if num in wMap:
                if wMap[num] == 1:
                    count += 1
                    wMap[num] = 2
            else:
                wMap[num] = 1
                count += 1
        nums = []
        for num in sorted(wMap):
            nums.extend([num] * wMap.get(num))
        return count

sol = Solution()
print sol.removeDuplicates([1,1,1,2])
