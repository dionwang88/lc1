class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        map1, map2 = {}, {}
        for num in nums1:
            if num in map1:
                map1[num] += 1
            else:
                map1[num] = 1
        for num in nums2:
            if num in map2:
                map2[num] += 1
            else:
                map2[num] = 1
        for num in map1:
            for i in xrange(map1[num]):
                if num in map2:
                    if map2[num] > 0:
                        map2[num] -= 1
                        res.append(num)
        return res
