# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    '''
    desc : https://discuss.leetcode.com/topic/39834/step-by-step-tackling-of-the-problem
    '''
    def __init__(self):
        self.rmap = {}

    def rob(self, root):
        if not root:
            return 0
        val = 0
        if root.left:
            val += self.rob(root.left.left) + self.rob(root.left.right)
        if root.right:
            val += self.rob(root.right.left) + self.rob(root.right.right)
        return max(val + root.val, self.rob(root.left) + self.rob(root.right))

    def robWithMemo(self, root):
        if not root:
            return 0
        if root in self.rmap:
            return self.rmap[root]
        val = 0
        if root.left:
            val += self.robWithMemo(root.left.left) + self.robWithMemo(root.left.right)
        if root.right:
            val += self.robWithMemo(root.right.left) + self.robWithMemo(root.right.right)
        val = max(val + root.val, self.robWithMemo(root.left) + self.robWithMemo(root.right))
        self.rmap[root] = val
        return val

    def robDP(self, root):
        res = self.robSub(root)
        return max(res)

    def robSub(self, root):
        if not root:
            return [0, 0]
        left = self.robSub(root.left)
        right = self.robSub(root.right)
        res = [0, 0]
        res[0] = max(left[0], left[1]) + max(right[0], right[1])
        res[1] = root.val + left[0] + right[0]
        return res
