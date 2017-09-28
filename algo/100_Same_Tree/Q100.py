# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class SameTree(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        stack = [(p, q)]
        while stack:
            x, y = stack.pop()
            if x == None and y == None:
                continue
            if x == None or y == None:
                return False
            if x.val == y.val:
                stack.append((x.left, y.left))
                stack.append((x.right, y.right))
            else:
                return False
        return True

st = SameTree()
root1 = TreeNode(0)
node11 = TreeNode(1)
node12 = TreeNode(2)
node13 = TreeNode(3)
node14 = TreeNode(4)
root1.left = node11
root1.right = node12
node11.left = node13
node11.right = node14

root2 = TreeNode(0)
node21 = TreeNode(1)
node22 = TreeNode(2)
node23 = TreeNode(3)
node24 = TreeNode(4)
root2.left = node21
root2.right = node22
node21.left = node23
node21.right = node24
print st.isSameTree(root1, root2)
