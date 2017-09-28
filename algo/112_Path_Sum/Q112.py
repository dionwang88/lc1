# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def hasPathSum(self, root, s):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        return self.dfs(root, 0, s)

    def dfs(self, root, total, s):
        if not root.left and not root.right:
            total += root.val
            if total == s:
                return True
            return False
        total += root.val
        left, right = False, False
        if root.left:
            left = self.dfs(root.left, total, s)
        if root.right:
            right = self.dfs(root.right, total, s)
        return left or right

node1 = TreeNode(1)
node2 = TreeNode(-2)
node3 = TreeNode(-3)
node4 = TreeNode(1)
node5 = TreeNode(3)
node6 = TreeNode(-2)
node8 = TreeNode(-1)
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node4.left = node8
sol = Solution()
print sol.hasPathSum(node1, 2)
