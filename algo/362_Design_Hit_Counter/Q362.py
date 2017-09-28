class Solution:
    def __init__(self):
        self.times = [1] * 300
        self.hits = [1] * 300

    def hit(self, timestamp):
        '''
        方法一：
        最直接的方法就是用一个队列queue，每次点击时都将当前时间戳加入queue中，然后在需要获取点击数时，
        我们从队列开头开始看，如果开头的时间戳在5分钟以外了，就删掉，直到开头的时间戳在5分钟以内停止，
        然后返回queue的元素个数即为所求的点击数
        
        方法二：
        定义了两个大小为300的一维数组times和hits，分别用来保存时间戳和点击数，在点击函数中，
        将时间戳对300取余，然后看此位置中之前保存的时间戳和当前的时间戳是否一样，一样说明是同一个时间戳，
        那么对应的点击数自增1，如果不一样，说明已经过了五分钟了，那么将对应的点击数重置为1。
        那么在返回点击数时，我们需要遍历times数组，找出所有在5分中内的位置，然后把hits中对应位置的点击数都加起来即可
        '''
        index = timestamp % 300
        if self.times[index] != timestamp:
            self.times[index] = timestamp
            self.hits[index] = 1
        else:
            self.hits[index] += 1

    def getHits(self, timestamp):
        res = 0
        for t in xrange(len(self.times)):
            if timestamp - self.times[i] < 300:
                res += self.hits[i]
        return res
