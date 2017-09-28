# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ret = []
        if not root:
            return ret
        import Queue as Q
        q = Q.Queue()
        q.put(root)
        while not q.empty():
            temp = []
            newRet = []
            for i in xrange(q.qsize()):
                node = q.get()
                temp.append(node.val)
                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)
            newRet.append(temp)
            newRet.extend(ret)
            ret = newRet
        return ret

node1 = TreeNode(3)
node2 = TreeNode(9)
node3 = TreeNode(20)
node4 = TreeNode(15)
node5 = TreeNode(7)
node1.left = node2
node1.right = node3
node3.left = node4
node3.right = node5

sol = Solution()
print sol.levelOrderBottom(node1)
