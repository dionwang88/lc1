'''
这道题让我们求二叉树的最长连续序列，关于二叉树的题基本都需要遍历树，而递归遍历写起来特别简单，
下面这种解法是用到了递归版的先序遍历，我们对于每个遍历到的节点，我们看节点值是否比参数值
(父节点值)大1，如果是则长度加1，否则长度重置为1，然后更新结果res，再递归调用左右子节点即可，
'''
class Solution:
    def __init__(self):
        self.max = 0
    def longestConsecutive(self, root):
        if not root:
            return 0
        dfs(root, 0, root.val)
        return self.max

    def dfs(self, root, cur, target):
        if not root:
            return
        if root.val == target:
            cur += 1
        else:
            cur = 1
        self.max = max(cur, self.max)
        dfs(root.left, cur, root.val + 1)
        dfs(root.right, cur, root.val + 1)

'''
下面这种写法是利用分治法的思想，对左右子节点分别处理，如果左子节点存在且节点值比其父节点值大1，
则递归调用函数，如果节点值不是刚好大1，则递归调用重置了长度的函数，对于右子节点的处理情况和左子节点相同
'''
class Solution1:
    def __init__(self):
        self.max = 0
    def longestConsecutive(self, root):
        if not root:
            return 0
        dfs(root, 1)
        return self.max

    def dfs(self, root, length):
        self.max = max(res, self.max)
        if root.left:
            if root.left.val == root.val + 1:
                dfs(root.left, length + 1)
            else:
                dfs(root.left, 1)
        if root.right:
            if root.right.val == root.val + 1:
                dfs(root.right, length + 1)
            else:
                dfs(root.right, 1)
