class Solution:
    def __init__(self):
        self.ret = False

    def palindrom(self, s):
        if len(s) <= 1:
            return True
        self.dfs(s, [])
        return self.ret

    def dfs(self, s, path):
        if not s:
            if self.isPalindrome(path):
                self.ret = True
            return

        for i in xrange(len(s)):
            if self.ret:
                break
            self.dfs(s[:i] + s[i + 1:], path + [s[i]])

    def isPalindrome(self, s):
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    def palindrom1(self, s):
        if len(s) <= 1:
            return True
        cmap = {}
        for c in s:
            if c in cmap:
                cmap[c] = cmap[c] + 1
            else:
                cmap[c] = 1
        count = 0
        for m in cmap:
            if cmap[m] % 2 == 1:
                count += 1
        if count <= 1:
            return True
        return False

sol = Solution()
print sol.palindrom1('aab')
