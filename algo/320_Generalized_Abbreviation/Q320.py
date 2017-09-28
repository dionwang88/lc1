class Solution:

    def generateAbbreviations(self, word):
        '''
        The idea is: for every character, we can keep it or abbreviate it. To keep it, we add it to the current
        solution and carry on backtracking. To abbreviate it, we omit it in the current solution, but increment the count,
        which indicates how many characters have we abbreviated. When we reach the end or need to put a character
        in the current solution, and count is bigger than zero, we add the number into the solution.
        :param word:
        :return:
        '''
        ret = []
        self.backtrack(ret, word, 0, '', 0)
        return ret

    def backtrack(self, ret, word, pos, cur, count):
        if pos == len(word):
            if count > 0:
                cur += str(count)
            ret.append(cur)
        else:
            self.backtrack(ret, word, pos + 1, cur, count + 1)
            if count > 0:
                cur += str(count)
            self.backtrack(ret, word, pos + 1, cur + word[pos], 0)

sol = Solution()
print sol.generateAbbreviations('word')
