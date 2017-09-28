class MergeSort:
    def __init__(self, B):
        self.B = B

    def mergeSort(self):
        lo, hi = 0, len(self.B) - 1
        self.sort(lo, hi)
        return self.B

    def sort(self, lo, hi):
        if lo < hi:
            mid = (lo + hi) / 2
            self.sort(lo, mid)
            self.sort(mid + 1, hi)
            self.merge(lo, mid, hi)

    def merge(self, lo, mid, hi):
        temp = []
        i, j = lo, mid + 1
        while i <= mid and j <= hi:
            if self.B[i] < self.B[j]:
                temp.append(self.B[i])
                i += 1
            else:
                temp.append(self.B[j])
                j += 1
        while i <= mid:
            temp.append(self.B[i])
            i += 1
        while j <= hi:
            temp.append(self.B[j])
            j += 1
        for k in xrange(len(temp)):
            self.B[k + lo] = temp[k]

ms = MergeSort([4,2,2,4,5,6,7,3,2])
print ms.mergeSort()
