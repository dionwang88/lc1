class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r, ret = 0, len(height) - 1, 0
        maxLeft, maxRight = 0, 0
        while l <= r:
            if height[l] <= height[r]:
                if height[l] >= maxLeft:
                    maxLeft = height[l]
                else:
                    ret += maxLeft - height[l]
                l += 1
            else:
                if height[r] >= maxRight:
                    maxRight = height[r]
                else:
                    ret += maxRight - height[r]
                r -= 1
        return ret
