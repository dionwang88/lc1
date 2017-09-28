import sys

class MinStack:
    def __init__(self):
        self.minVal = sys.maxint
        self.minStack = []

    '''
    push的时候计算一下最小值
    pop的时候再计算一下最小值
    '''
    def push(self, item):
        self.minStack.append(item)
        self.minVal = min(self.minVal, item)

    def top(self):
        return self.minStack[-1]

    def pop(self):
        top = self.minStack.pop()
        if top == self.minVal:
            self.minVal = sys.maxint
            for item in self.minStack:
                self.minVal = min(self.minVal, item)
        return top

    def getMin(self):
        return self.minVal

minstack = MinStack()
minstack.push(-2)
minstack.push(0)
minstack.push(-3)
print minstack.getMin()
print minstack.pop()
print minstack.top()
print minstack.getMin()
