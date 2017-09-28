# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root
        self.dfs(root)
        return root

    def dfs(self, root):
        if not root:
            return
        else:
            temp = root.left
            root.left = root.right
            root.right = temp
            self.dfs(root.left)
            self.dfs(root.right)
