class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        :desc: binary search
        """
        if (num < 1): return False;
        left, right = 1, num
        while left <= right:
            mid = left + (right - left) / 2
            t = mid * mid
            if t > num:
                right = mid - 1
            elif t < num:
                left = mid + 1
            else:
                return True
        return False
