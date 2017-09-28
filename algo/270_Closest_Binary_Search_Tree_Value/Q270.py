class Solution:
    def __init__(self):
        import sys
        self.minValue = sys.maxint
        self.closestValue = 0

    def closestValue(self, root, n):
        self.helper(root, n)
        return self.closestValue

    def helper(self, root, n):
        if not root:
            return
        if self.minValue < abs(n - root.val):
            self.minValue = abs(n - root.val)
            self.closestValue = root.val

        if root.val < n:
            self.helper(root.right, n)
        else:
            self.helper(root.left, n)

    def closestValue1(self, root, n):
        ret = root.val
        while not root:
            if abs(n - root.val) < abs(n - ret)
            ret = root.val
            root = root.val > n ? root.left : root.right
        return ret
