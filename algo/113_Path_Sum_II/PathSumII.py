# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        stack, path, ret = [], {}, []
        stack.append(root)
        path[root] = [root.val]
        while stack:
            node = stack.pop()
            left, right = node.left, node.right
            nodePath = path[node]
            if left != None:
                stack.append(left)
                nodePath = list(path[node])
                nodePath.append(left.val)
                path[left] = nodePath
            if right != None:
                stack.append(right)
                nodePath = list(path[node])
                nodePath.append(right.val)
                path[right] = nodePath
            if left == None and right == None:
                cost = 0
                for v in nodePath:
                    cost += v
                if cost == sum:
                    ret.append(nodePath)
        return ret
                
