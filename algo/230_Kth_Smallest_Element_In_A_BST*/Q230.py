# Definition for a binary tree node.
class TreeNodeWithCount(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.count = 1
        self.leftNum = 0
        self.order  = 0

class Solution(object):
    def __init__(self):
        self.count = 0
        self.number = 1

    def kthSmallest(self, root, k):
        """
        修改TreeNode添加该节点下的count
        """
        newRoot = self.buildTreeNodeWithCount(root)
        return self.kthSmallestHelper(newRoot, k)

    def kthSmallestHelper(self, root, k):
        if k <= 0 or k > root.count:
            return -1
        if root.left:
            if root.left.count >= k:
                return self.kthSmallestHelper(root.left, k)
            elif root.left.count == k - 1:
                return root.val
            else:
                return self.kthSmallestHelper(root.right, k - root.left.count - 1)
        else:
            if k == 1:
                return root.val
            return self.kthSmallestHelper(root.right, k - 1)

    def buildTreeNodeWithCount(self, root):
        if not root:
            return None
        newRoot = TreeNodeWithCount(root.val)

        newRoot.left = self.buildTreeNodeWithCount(root.left)
        newRoot.right = self.buildTreeNodeWithCount(root.right)
        if newRoot.left:
            newRoot.count += newRoot.left.count
        if newRoot.right:
            newRoot.count += newRoot.right.count
        return newRoot

    def kthSmallestOrder(self, root, k):
        '''
        desc: 直接记录节点的order更简单
        '''
        newRoot = self.buildTreeNodeWithOrder(root)
        return self.kthSmallestOrderHelper(newRoot, k)

    def kthSmallestOrderHelper(self, root, k):
        if k > root.order and not root.right:
            return -1
        if root.order == k:
            return root.val
        elif root.order > k:
            return self.kthSmallestOrderHelper(root.left, k)
        elif root.order < k and root.right:
            return self.kthSmallestOrderHelper(root.right, k)

    def buildTreeNodeWithOrder(self, root):
        '''
        用中序遍历创建新的树
        '''
        if not root:
            return None
        newRoot = TreeNodeWithCount(root.val)
        newRoot.left = self.buildTreeNodeWithOrder(root.left)
        newRoot.order = self.number
        self.number += 1
        newRoot.right = self.buildTreeNodeWithOrder(root.right)
        return newRoot

    def kthSmallest1(self, root, k):
        '''
        :desc: Binary Search (DFS)
        '''
        def countNodes(root):
            if not root:
                return 0
            return 1 + countNodes(root.left) + countNodes(root.right)
        count = countNodes(root.left)
        if k <= count:
            return self.kthSmallest1(root.left, k)
        elif k > count + 1:
            return self.kthSmallest1(root.right, k - count - 1)
        return root.val

    def kthSmallest2(self, root, k):
        '''
        desc: DFS in-order recursive
        '''
        self.count = k
        helper(root)
        return self.number

    def helper(root):
        if root.left:
            helper(root.left)
        self.count -= 1
        if self.count == 0:
            self.number = root.val
            return
        if root.right:
            helper(root.right)

    def kthSmallest3(self, root, k):
        '''
        desc: DFS in-order Iterative, first to find the most left, then pop it and if it has right, then find this right the most left node
        '''
        stack = []
        while root:
            stack.append(root)
            root = root.left
        while k != 0:
            node = stack.pop()
            k -= 1
            if k == 0:
                return node.val
            right = node.right
            while right:
                stack.append(right)
                right = right.left
        return -1
