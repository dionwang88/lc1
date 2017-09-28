class QuickSort:
    def __init__(self, A):
        self.A = A

    def quickSort(self, start, end):
        i, j, pivot = start, start, end
        while j < pivot:
            if self.A[j] <= self.A[pivot]:
                j += 1
            else:
                swap(i, j)
                i += 1
                j += 1
        if self.A[i] <= self.A[pivot]:
            swap(i, pivot)

        if (i > 0):
            quickSort(start, i-1);
        else:
            return;
        if (i < end):
            quickSort(i+1, end);
        else:
            return

    def swap(i, j):
        temp = self.A[i]
        self.A[i] = self.A[j]
        self.A[j] = temp
