class Solution:
    def __init__(self):
        self.res = []

    def findLeaves(self, root):
        self.dfs(root)
        return self.res

    def dfs(self, root):
        if not root:
            return -1
        int depth = 1 + max(dfs(root.left), dfs(root.right))
        if len(self.res) <= depth:
            self.res.append([])
        self.res[depth].append(root.val)
        return depth
