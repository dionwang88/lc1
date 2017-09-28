class Solution(object):
    def __init__(self):
        self.map = {}

    def diffWaysToCompute(self, inputs):
        if not inputs:
            return []
        return self.helper(inputs)

    def helper(self, inputs):
        res = []
        for i in xrange(len(inputs)):
            c = inputs[i]
            if c == '+' or c == '-' or c == '*':
                p1 = inputs[:i]
                p2 = inputs[i + 1:]
                l1 = self.map.get(p1, self.helper(p1))
                l2 = self.map.get(p2, self.helper(p2))
                for i1 in l1:
                    for i2 in l2:
                        r = 0
                        if c == '+':
                            r = i1 + i2
                        elif c == '-':
                            r = i1 - i2
                        elif c == '*':
                            r = i1 * i2
                        res.append(r)
        if len(res) == 0:
            res.append(int(inputs))
        self.map[inputs] = res
        return res

sol = Solution()
print sol.diffWaysToCompute('2*3-4*5')
