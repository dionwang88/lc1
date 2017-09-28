class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        areaOfA = (C - A) * (D - B)
        areaOfB = (G - E) * (H - F)
        left = max(A, E)
        right = min(G, C)
        bottom = max(F, B)
        top = min(D, H)

        # IF overlapping
        overlap = 0
        if right > left and top > bottom:
            overlap = (right - left) * (top - bottom)
        return areaOfA + areaOfB - overlap
