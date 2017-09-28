# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def sym_tree(L,R):
            if L and R:
                return L.val == R.val and sym_tree(L.left, R.right) and sym_tree(L.right, R.left)
            else:
                return L == R
        return sym_tree(root, root)

    def isSymmetric1(self, root):
        now = []
        if root:
            now.append(root)
        while now:
            vals = []
            for i in now:
                if i:
                    vals.append(i.val)
                else:
                    vals.append(None)
            if list(reversed(vals)) != vals:
                return False
            else:
                now = [j for i in now if i for j in (i.left, i.right)]
        return True
