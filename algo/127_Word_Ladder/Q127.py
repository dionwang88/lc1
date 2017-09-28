class Solution(object):
    def __init__(self):
        self.wmap = {}
        self.tmap = {}

    def ladderLength(self, beginWord, endWord, wordList):
        clist = list('abcdefghijklmnopqrstuvwxyz')
        wordList.add(beginWord)
        wordList.add(endWord)
        for word in wordList:
            for i in xrange(len(word)):
                for c in clist:
                    new_word = word[:i] + c + word[i + 1:]
                    if new_word in wordList:
                        self.addNewWord(word, new_word)
                        self.addNewWord(new_word, word)

        self.dfs(beginWord, endWord, [], wordList)
        return self.tmap[beginWord + endWord]

    def addNewWord(self, word, new_word):
        if word in self.wmap:
            sub_map = self.wmap[word]
            if new_word not in sub_map and new_word != word:
                sub_map[new_word] = 1
                self.wmap[word] = sub_map
        else:
            sub_map = {new_word: 1}
            self.wmap[word] = sub_map

    def dfs(self, beginWord, endWord, path, wordList):
        for word in wordList:
            if word == endWord:
                self.tmap[beginWord + endWord] = path + [word]
                return
            if word in self.wmap[beginWord]:
                self.dfs(word, endWord, path + [word], wordList)
        return

sol = Solution()
sets = set()
for item in ["hot", "dot", "dog", "lot", "log"]:
    sets.add(item)
print sol.ladderLength('hit', 'cog', sets)
