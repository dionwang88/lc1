class Solution:
    def wiggleSort(self, nums):
        '''
        Given an unsorted array nums, reorder it in-place such that nums[0] <= nums[1] >= nums[2] <= nums[3]....
        For example, given nums = [3, 5, 1, 4, 6, 2], one possible answer is [1, 6, 2, 5, 3, 4].
        我们可以先将数组排序，这时候从第3个元素开始，将第3个元素和第2个元素交换。
        然后再从第5个元素开始，将第5个元素和第4个元素交换，以此类推。就能满足题目要求。
        时间复杂度是O(nlog(n))
        '''
        nums = sorted(nums)
        for i in xrange(2, len(nums), 2):
            temp = nums[i - 1]
            nums[i - 1] = nums[i]
            nums[i] = temp
        print nums

    def wiggleSort1(self, nums):
        '''
        交换法：
        题目对摇摆排序的定义有两部分：
            1. 如果i是奇数，nums[i] >= nums[i - 1]
            2. 如果i是偶数，nums[i] <= nums[i - 1]
        所以我们只要遍历一遍数组，把不符合的情况交换一下就行了。
        时间复杂度O(n)， 空间复杂度O(1)
        '''
        for i in xrange(1, len(nums)):
            if (i % 2 == 1 and nums[i] < nums[i - 1]) or (i % 2 == 0 and nums[i] > nums[i - 1]):
                temp = nums[i - 1]
                nums[i - 1] = nums[i]
                nums[i] = temp

sol = Solution()
sol.wiggleSort1([3, 5, 1, 4, 6, 2])
