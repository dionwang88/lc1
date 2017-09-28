# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        n = len(preorder) - 1
        inMap = {}
        for i in xrange(len(inorder)):
            inMap[inorder[i]] = i
        root = self.build(preorder, 0, n, inorder, 0, n, inMap)
        return root

    def build(self, preorder, pre_st, pre_end, inorder, in_st, in_end, inMap):
        if pre_st > pre_end or in_st > in_end:
            return None
        root = TreeNode(preorder[pre_st])
        inRoot = inMap[root.val]
        numsLeft = inRoot - in_st

        root.left = self.build(preorder, pre_st + 1, pre_st + numsLeft, inorder, in_st, inRoot - 1, inMap)
        root.right = self.build(preorder, pre_st + numsLeft + 1, pre_end, inorder, inRoot + 1, in_end, inMap)
        return root
        
