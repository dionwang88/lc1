class Solution:
    def __init__(self, vec2d):
        self.vec = vec2d
        self.row = 0
        self.col = 0

    def next(self):
        if self.hasNext():
            if self.col < len(self.vec[self.row]) - 1:
                res = self.vec[self.row][self.col + 1]
                self.col += 1
                return res
            elif self.col == len(self.vec[self.row]) - 1:
                self.col = 0
                self.row += 1
                res = self.vec[self.row][self.col]
                return res
        return None

    def hasNext(self):
        if self.row < len(self.vec) - 1:
            return True
        elif self.row == len(self.vec) - 1:
            if self.col < len(self.vec[self.row]) - 1:
                return True
        return False
