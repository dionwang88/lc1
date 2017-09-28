import sys

class Solution:
    def verifyPreorder(self, preorder):
        stack = []
        minVal = -sys.maxint
        for num in preorder:
            if num < minVal:
                return False
            while len(stack) > 0 and num > stack[-1]:
                minVal = stack.pop()
            stack.append(num)
        return True

sol = Solution()
print sol.verifyPreorder([6,3,1,2,5,4,7])
