class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.res = []

    def rightSideView(self, root):
        '''
        The core idea of this algorithm:
            1. Each depth of the tree only select one node.
            2. View depth is current size of result list.
        '''
        if not root:
            return self.res
        self.getRightView(root, 0)
        return self.res

    def getRightView(self, root, curDepth):
        if not root:
            return
        if curDepth == len(self.res):
            self.res.append(root.val)
        self.getRightView(root.right, curDepth + 1)
        self.getRightView(root.left, curDepth + 1)

node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)
node8 = TreeNode(8)
node9 = TreeNode(9)

node1.right = node2
node2.right = node5
node5.right = node6
node5.left = node4
node4.left = node3

sol = Solution()
sol.rightSideView(node1)
