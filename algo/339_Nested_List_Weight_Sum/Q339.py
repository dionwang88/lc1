class Solution:
    def __init__(self):
        self.total = 0

    def getSum(self, nestedList):
        if not nestedList:
            return 0
        for l in nestedList:
            self.dfs(l, 1)
        return self.total

    def dfs(self, nestedList, depth):
        if type(nestedList) == list:
            for l in nestedList:
                if type(l) == list:
                    self.dfs(l, depth + 1)
                else:
                    self.total += l * (depth + 1)
        else:
            self.total += nestedList * depth

sol = Solution()
print sol.getSum([1,[4,[6]]])
