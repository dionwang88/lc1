class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def upsideDownBinaryTree(self, root):
        '''
        解法一：将左子树递归颠倒，然后原来的左孩子的左右孩子指针分别指向原来的右兄弟和原来的根节点
        这个题目可以这样做的关键是树的任何一个右孩子都没有枝节，基本就是一个梳子的形状，所以不用递归右子树
        '''
        if not root:
            return None
        parent, left, right = root, root.left, root.right
        if left:
            ret = self.upsideDownBinaryTree(left)
            left.left = right
            left.right = parent
            return ret
        return root

    def upsideDownBinaryTree1(self, root):
        '''
        解法二：迭代方法，借助stack做中序遍历
        '''
        if not root:
            return None
        stack = []
        node, left, right = root, None, None
        while node.left:
            stack.append(node)
            node = node.left
        root = node
        while len(stack) > 0:
            parent = stack.pop()
            right = parent.right
            node.left = right
            node.right = parent
            node = parent
        right.left = None
        right.right = None
        node.left = None
        node.right = None
        return root

sol = Solution()

node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5

sol.upsideDownBinaryTree1(node1)
