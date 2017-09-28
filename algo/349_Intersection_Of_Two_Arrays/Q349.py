class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        map1, map2 = {}, {}
        for i in nums1:
            map1[i] = 1
        for i in nums2:
            map2[i] = 1
        for i in map1:
            if i in map2:
                res.append(i)

        return res
