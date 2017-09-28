class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        :desc: bucket sorting
        """
        bucket = [None] * (len(nums) + 1)
        nmap = {}
        for num in nums:
            nmap[num] = nmap.get(num, 0) + 1
        for key in nmap:
            frequency = nmap[key]
            if not bucket[frequency]:
                bucket[frequency] = []
            bucket[frequency].append(key)
        res = []
        for i in xrange(len(bucket) - 1, -1, -1):
            if len(res) == k:
                break
            if bucket[i]:
                res.extend(bucket[i])
        return res

sol = Solution()
print sol.topKFrequent([1,1,1,2,2,2,2,3,4,5,6,6,6,6], 3)
