class Solution:
    def sortTransformedArray(self, nums, a, b, c):
        '''
        当a>0，说明两端的值比中间的值大，那么此时我们从结果res后往前填数，用两个指针分别指向nums数组的开头和结尾，
        指向的两个数就是抛物线两端的数，将它们之中较大的数先存入res的末尾，然后指针向中间移，重复比较过程，直到把res都填满。
        当a<0，说明两端的值比中间的小，那么我们从res的前面往后填，用两个指针分别指向nums数组的开头和结尾，指向的两个数就是抛物线两端的数，
        将它们之中较小的数先存入res的开头，然后指针向中间移，重复比较过程，直到把res都填满。
        当a=0，函数是单调递增或递减的，那么从前往后填和从后往前填都可以，我们可以将这种情况和a>0合并。
        '''
        res = [0] * len(nums)
        if not nums:
            return res
        left, right = 0, len(nums) - 1
        index = len(nums) - 1 if a >= 0 else 0
        while left <= right:
            lval = a * nums[left] * nums[left] + b * nums[left] + c
            rval = a * nums[right] * nums[right] + b * nums[right] + c
            if a >= 0:
                if lval >= rval:
                    res[index] = lval
                    left += 1
                else:
                    res[index] = rval
                    right -= 1
                index -= 1
            else:
                if lval >= rval:
                    res[index] = rval
                    right -= 1
                else:
                    res[index] = lval
                    left += 1
                index += 1
        return res

sol = Solution()
print sol.sortTransformedArray([-4, -2, 2, 4], -1, 3, 5)
