class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if not nums:
            return False
        if len(nums) == 1:
            return nums[0] == target

        start, end = 0, len(nums) - 1
        while start <= end:
            mid = start + (end - start) / 2
            if nums[mid] == target:
                return True
            # If we know for sure right side is sorted or left side is unsorted
            if (nums[mid] < nums[end] or nums[mid] < nums[start]):
                if target > nums[mid] and target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
            # If we know for sure left side is sorted or right side is unsorted
            elif nums[mid] > nums[start] or nums[mid] > nums[end]:
                if target < nums[mid] and target >= nums[start]:
                    end = mid - 1
                else:
                    start = mid + 1
            # If we get here, that means nums[start] == nums[mid] == nums[end], then shifting out
            # any of the two sides won't change the result but can help remove duplicate from
            # consideration, here we just use end-- but left++ works too
            else:
                end -= 1

        return False

sol = Solution()
print sol.search([1,1], 3)
