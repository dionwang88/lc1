class MovingAverage:
    def __init__(self, size):
        import Queue
        self.size = size
        self.q = Queue.Queue()
        self.sum = 0

    def next(self, val):
        if self.q.qsize() < self.size:
            self.q.put(val)
            self.sum += val
            return (self.sum * 1.0) / self.q.qsize()
        else:
            self.sum -= self.q.get()
            self.q.put(val)
            self.sum += val
            return (self.sum * 1.0) / self.q.qsize()

sol = MovingAverage(3)
print sol.next(1)
print sol.next(3)
print sol.next(2)
print sol.next(3)
print sol.next(4)
