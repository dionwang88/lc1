class Solution:
    def __init__(self):
        # With Memorization:
        self.memo = {}

    def canWin(self, s):
        if not s:
            return False
        return self.helper(list(s))

    def helper(self, chars):
        key = ''.join(chars)
        win = False
        if key not in self.memo:
            for i in xrange(len(chars) - 1):
                if chars[i] == '+' and chars[i + 1] == '+':
                    chars[i] = chars[i + 1] = '-'
                    win = not self.helper(chars)
                    chars[i] = chars[i + 1] = '+'
                    if win:
                        return True
        self.memo[key] = win
        return self.memo[key]

sol = Solution()
print sol.canWin('+--++-+--+')
