class Solution:
    def __init__(self):
        self.count = 0

    def countUnivalueSubtrees(self, root):
        self.dfs(root)
        return self.count

    def dfs(self, root):
        if not root:
            return True

        if not root.left and not root.right:
            self.count += 1
            return True

        leftStatus = self.dfs(root.left)
        rightStatus = self.dfs(root.right)
        if not leftStatus or not rightStatus:
            return False
        if (not root.left or root.val == root.left.val) and (not root.right or root.val == root.right.val):
            self.count += 1
            return True
        else:
            return False
