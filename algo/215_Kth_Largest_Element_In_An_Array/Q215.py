class Solution(object):
    def findKthLargest(self, nums, k):
        if not nums or k < 1 or k > len(nums):
            return 0
        low, high = 0, len(nums) - 1
        while low < high:
            pivot = self.partition(nums, low, high)
            if pivot == k - 1:
                return nums[pivot]
            elif pivot > k - 1:
                high = pivot - 1
            else:
                low = pivot + 1

    def partition(self, nums, i, j):
        k, pivot = i, j
        while k <= j:
            if nums[k] > nums[pivot]:
                self.swap(nums, i, k)
                i += 1
            k += 1
        self.swap(nums, i, pivot)
        return i

    def swap(self, nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp

sol = Solution()
print sol.findKthLargest([7,6,5,4,8,9,1], 5)
