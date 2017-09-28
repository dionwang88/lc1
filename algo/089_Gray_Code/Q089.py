class Solution:
    def gray_code(self, n):
        arr = []
        arr.append(0)
        for i in xrange(n):
            inc = 1 << i
            for j in xrange(len(arr) - 1, -1, -1):
                arr.append(arr[j] + inc)
        return arr

sol = Solution()
print sol.gray_code(4)
