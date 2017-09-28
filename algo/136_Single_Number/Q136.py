class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        known that A XOR A = 0 and the XOR operator is commutative, the solution will be very straightforward.
        """
        res = 0
        for i in nums:
            res ^= i
        return res
