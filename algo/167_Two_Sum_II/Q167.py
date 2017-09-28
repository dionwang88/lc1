class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        利用二分法
        """
        import sys
        res = []
        if not numbers or len(numbers) < 2 or target > 2 * numbers[len(numbers) - 1]:
            return res

        if target == 0 and numbers[0] == 0:
            if numbers[1] != 0:
                return res
            else:
                return [1, 2]

        low, high = 0, len(numbers) - 1
        dist, index = sys.maxint, -1

        while low < high:
            mid = low + (high - low) / 2
            if numbers[mid] < target:
                low = mid + 1
            else:
                high = mid
                if numbers[mid] - target < dist:
                    dist = numbers[mid] - target
                    index = mid
        if low == high == len(numbers) - 1:
            index = high

        for i in xrange(index + 1):
            tar = target - numbers[i]
            low, high = 0, index
            while low < high:
                mid = low + (high - low) / 2
                if numbers[mid] < tar:
                    low = mid + 1
                elif numbers[mid] > tar:
                    high = mid
                elif numbers[mid] == tar and mid != i:
                    return [min(i, mid) + 1, max(i, mid) + 1]
            if low == high == index and numbers[low] == tar:
                return [i + 1, low + 1]

        return res

    def twoSum1(self, nums, target):
        res = []
        if len(nums) < 2:
            return res
        left, right = 0, len(nums) - 1
        while left < right:
            v = nums[left] + nums[right]
            if v == target:
                return [left + 1, right + 1]
            elif v > target:
                right -= 1
            else:
                left += 1
        return res

sol = Solution()
print sol.twoSum([0,2,4,90], 2)
