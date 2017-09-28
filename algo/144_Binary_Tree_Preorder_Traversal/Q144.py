# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        ret, stack = [], []
        if not root:
            return ret
        stack.append(root)

        while len(stack) > 0:
            node = stack.pop()
            ret.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return ret

node1 = TreeNode(1)
node4 = TreeNode(4)
node2 = TreeNode(2)
node3 = TreeNode(3)
node1.left = node4
node1.right = node2
node2.left = node3

sol = Solution()
print sol.preorderTraversal(node1)
