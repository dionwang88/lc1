class Solution:
    def __init__(self):
        self.lmap = {}
        self.maxLevel = 0

    def depthSumInverse(self, nestedList):
        if not nestedList:
            return 0
        res = 0
        self.helper(nestedList, 1)
        for level in self.lmap:
            for num in self.lmap[level]:
                res += (self.maxLevel - level + 1) * num
        return res

    def helper(self, nestedList, level):
        self.maxLevel = max(self.maxLevel, level)
        if type(nestedList) == int:
            if level in self.lmap:
                temp = self.lmap[level]
                temp.append(nestedList)
                self.lmap[level] = temp
            else:
                temp = []
                temp.append(nestedList)
                self.lmap[level] = temp
            return
        else:
            for l in nestedList:
                self.helper(l, level + 1)

    def depthSumInverse1(self, nestedList):
        '''
        下面这个方法就比较巧妙了，由史蒂芬大神提出来的，这个方法用了两个变量unweighted和weighted，非权重和跟权重和，初始化均为0，
        然后如果nestedList不为空开始循环，先声明一个空数组nextLevel，遍历nestedList中的元素，如果是数字，则非权重和加上这个数字，
        如果是数组，就加入nextLevel，这样遍历完成后，第一层的数字和保存在非权重和unweighted中了，其余元素都存入了nextLevel中，
        此时我们将unweighted加到weighted中，将nextLevel赋给nestedList，这样再进入下一层计算，由于上一层的值还在unweighted中，
        所以第二层计算完将unweighted加入weighted中时，相当于第一层的数字和被加了两次，这样就完美的符合要求了，这个思路又巧妙又牛B，大神就是大神啊
        '''
        if not nestedList:
            return 0
        nextLevel = list(nestedList)
        unweighted, weighted = 0, 0
        while len(nextLevel) > 0:
            temp = []
            for item in nextLevel:
                if type(item) == int:
                    unweighted += item
                else:
                    for l in item:
                        temp.append(l)
            nextLevel = temp
            weighted += unweighted
        return weighted

sol = Solution()
print sol.depthSumInverse1([1,[2, [4, [5]]]])
