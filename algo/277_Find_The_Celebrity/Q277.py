class Solution:
    def findCelebrity(self, n):
        '''
        The key part is the first loop. To understand this you can think the
        knows(a,b) as a a < b comparison, if a knows b then a < b, if a does
        not know b, a > b. Then if there is a celebrity, he/she must be the
        "maximum" of the n people.
        However, the "maximum" may not be the celebrity in the case of no
        celebrity at all. Thus we need the second and third loop to check
        if x is actually celebrity by definition.
        '''
        x = 0
        for i in xrange(n):
            if knows(x, i):
                x = i
        for i in xrange(x):
            if knows(x, i):
                return -1
        for i in xrange(n):
            if not knows(i, x):
                return -1
        return x
