class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        https://discuss.leetcode.com/topic/8398/dp-solution-in-6-lines-with-explanation-f-i-n-g-i-1-g-n-i/2
        """
        G = [0] * (n + 1)
        G[0], G[1] = 1, 1
        for i in xrange(2, n + 1):
            for j in xrange(1, i + 1):
                G[i] += G[j - 1] * G[i- j]

        return G[n]
