class Solution:
    def lengthOfLIS(self, nums):
        '''
        http://www.cnblogs.com/grandyang/p/4938187.html
        下面我们来看一种优化时间复杂度到O(nlgn)的解法，这里用到了二分查找法，所以才能加快运行时间哇。
        思路是，我们先建立一个数组ends，把首元素放进去，然后比较之后的元素，如果遍历到的新元素比ends
        数组中的首元素小的话，替换首元素为此新元素，如果遍历到的新元素比ends数组中的末尾元素还大的话，
        将此新元素添加到ends数组末尾(注意不覆盖原末尾元素)。如果遍历到的新元素比ends数组首元素大，
        比尾元素小时，此时用二分查找法找到第一个不小于此新元素的位置，覆盖掉位置的原来的数字，
        以此类推直至遍历完整个nums数组，此时ends数组的长度就是我们要求的LIS的长度，特别注意的是ends
        数组的值可能不是一个真实的LIS，比如若输入数组nums为{4, 2， 4， 5， 3， 7}，那么算完后的
        ends数组为{2， 3， 5， 7}，可以发现它不是一个原数组的LIS，只是长度相等而已，千万要注意这点。
        注意这个二分查找第一个不小于该数的方法
        '''
        if len(nums) == 0:
            return 0
        ends = []
        ends[0] = nums[0]
        for a in nums:
            if a < ends[0]:
                ends[0] = a
            elif a > ends[-1]:
                ends.append(a)
            else:
                left, right = 0, len(ends)
                while left < right:
                    mid = left + (right - left) / 2
                    if ends[mid] < a:
                        left = mid + 1
                    else:
                        right = mid
                ends[right] = a
        return len(ends)
