import Queue as Q

class Node:
   def __init__(self, it):
      self.it = it
      self.val = it.next()
   def __cmp__(self, other):
      return cmp(self.val, other.val)

class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        :DESC:  Time Limit Exceeded
        """
        if not matrix or not matrix[0]:
            return 0
        n, m = len(matrix), len(matrix[0])
        minHeap = Q.PriorityQueue()
        for l in matrix:
           minHeap.put(Node(iter(l)))
        count = 0
        while minHeap.qsize() > 0:
           node = minHeap.get()
           val = node.val
           count += 1
           if count == k:
               return val
           newVal = next(node.it, None)
           if newVal != None:
               node.val = newVal
               minHeap.put(node)

matrix = [[0,0,0],[2,7,9],[7,8,11]]
sol = Solution()
print sol.kthSmallest(matrix, 7)
