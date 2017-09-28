# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        if not root:
            return []
        res, stack = [], []
        while root:
            stack.append(root)
            root = root.left
        while len(stack) > 0:
            node = stack.pop()
            res.append(node.val)
            right = node.right
            if right:
                stack.append(right)
                node = right.left
                while node:
                    stack.append(node)
                    node = node.left
        return res

node1 = TreeNode(1)
node4 = TreeNode(4)
node2 = TreeNode(2)
node3 = TreeNode(3)
node1.left = node4
node1.right = node2
node2.left = node3

sol = Solution()
print sol.inorderTraversal(node1)
