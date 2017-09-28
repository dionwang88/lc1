import sys

class Solution:
    def maxSubArrayLen(self, nums, k):
        '''
        Use a HashMap to keep track of the sum from index 0 to index i, use it as the key,
        and use the current index as the value
        build the hashmap: scan from left to write, if the current sum does not exist in the hashmap,
        put it in. If the current sum does exist in Hashmap, do not replace or add to the older value,
        simply do not update. Because this value might be the left index of our subarray in later comparison.
        We are looking for the longest subarray so we want the left index to be the smaller the better.
        Every time we read a number in the array, we check to see if map.containsKey(num-k), if yes, try to update the maxLen.
        '''
        if len(nums) < 0:
            return 0
        smap = {0: -1}
        subSum = 0
        maxLen = sys.maxint
        for i in xrange(len(nums)):
            subSum += nums[i]
            if subSum not in smap:
                smap[subSum] = i
            if subSum - k in smap:
                maxLen = max(maxLen, smap[subSum - k])
        return 0 if maxLen == sys.maxint else maxLen

sol = Solution()
print sol.maxSubArrayLen([1, -1, 5, -2, 3], 3)