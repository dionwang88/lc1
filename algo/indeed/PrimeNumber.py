class PrimeNumber:
    def __init__(self, number):
        self.number = number
    def prime(self):
        from math import sqrt
        num = self.number
        sqrtNum = int(sqrt(num)) + 1
        numMap = {}
        for i in xrange(num + 1):
            numMap[i] = 0
        for i in xrange(2, sqrtNum):
            for j in xrange(3, num + 1):
                if j % i == 0:
                    if numMap[j] == 0:
                        numMap[j] = 1
        for i in numMap:
            if numMap[i] == 0:
                print i,

pn = PrimeNumber(1000)
pn.prime()
