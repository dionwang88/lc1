class QuickSelect:
    def __init__(self, A):
        self.A = A

    def quickSelect(self, start, end, k):
        '''
        QuickSelect的核心是partition方法
        每次partition之后，要判断pivot的位置
        '''
        i, j = start, end
        while True:
            pivot = self.partition(i, j)
            if pivot == k - 1:
                return self.A[pivot]
            elif pivot > k - 1:
                j = pivot - 1
            else:
                i = pivot + 1
        return -1

    def swap(self, i, j):
        temp = self.A[i]
        self.A[i] = self.A[j]
        self.A[j] = temp

    def partition(self, start, end):
        i, j, pivot = start, start, end
        while j < pivot:
            if self.A[j] >= self.A[pivot]:
                j += 1
            else:
                self.swap(i, j)
                i += 1
                j += 1
        return i

l = [7,2,4,5,9,1,3,6,10,8]
qs = QuickSelect(l)
print qs.quickSelect(0, len(l) - 1, 4)
