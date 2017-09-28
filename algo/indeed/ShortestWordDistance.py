class WordDistance:
    def __init__(self, wordList):
        self.wordMap = {}
        for i in xrange(len(wordList)):
            word = wordList[i]
            if word in self.wordMap:
                wl = self.wordMap[word]
                wl.append(i)
                self.wordMap[word] = wl
            else:
                self.wordMap[word] = [i]

    def wordDistanceI(self, wordList, word1, word2):
        import sys
        idx1, idx2 = -1, -1
        minDistance = sys.maxint
        for i in xrange(wordList):
            if wordList[i] == word1:
                idx1 = i
            elif wordList[i] == word2:
                idx2 = i
            if idx1 != -1 and idx2 != -1:
                minDistance = min(minDistance, abs(idx2 - idx1))
        return minDistance

    '''
    Given a list of words and two words word1 and word2, return the shortest
    distance between these two words in the list.

    For example, Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

    Given word1 = "coding", word2 = "practice", return 3.
    Given word1 = "makes", word2 = "coding", return 1.
    '''
    def wordDistanceII(self, wordList, word1, word2):
        import sys
        '''
        count用来控制相同的word的顺序
        '''
        idx1, idx2, count, minDistance = -1, -1, 0, sys.maxint
        for i in xrange(len(wordList)):
            if wordList[i] == word1 and count % 2 == 0:
                idx1 = i
                count += 1
            elif wordList[i] == word2 and count % 2 == 1:
                idx2 = i
                count = 0
            if idx1 != -1 and idx2 != -1:#不要忘了检测index值
                minDistance = min(minDistance, abs(idx2 - idx1))
        return minDistance

    def wordDistanceIII(self, word1, word2):
        '''
        This is a follow up of Shortest Word Distance. The only difference is now you
        are given the list of words and your method will be called repeatedly many times
         with different parameters. How would you optimize it?

        Design a class which receives a list of words in the constructor, and implements
        a method that takes two words word1 and word2 and return the shortest distance
        between these two words in the list.
        The key idea is to store the indexes of each word using a hash map. Then the
        function shortest() is just to find the minimum difference between two sorted lists
        '''
        import sys
        minDistance = sys.maxint
        wl1 = self.wordMap[word1]
        wl2 = self.wordMap[word2]
        wl1.sort()
        wl2.sort()
        i, j = 0, 0
        if word1 != word2:
            while i < len(wl1) and j < len(wl2):
                minDistance = min(minDistance, abs(wl1[i] - wl2[j]))
                if wl1[i] < wl2[j]:
                    i += 1
                else:
                    j += 1
        else:
            if len(wl1) > 1:
                for i in xrange(1, len(wl1)):
                    minDistance = min(minDistance, (wl1[i] - wl1[i - 1]))
            else:
                minDistance = -1
        return minDistance

wordList = ["practice", "makes", "perfect", "coding", "makes"]
word1 = "practice"
word2 = "perfect"
# wd = WordDistanceII(wordList)
# print wd.wordDistanceII(word1, word2)
