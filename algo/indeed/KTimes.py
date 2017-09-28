class Node:
    def __init__(self, ite):
        self.ite = ite
        self.val = ite.next()
    def __cmp__(self, other):
        return cmp(self.val, other.val)

class KTimes:
    def ktimes(self, lst, k):
        ret, count = [], 1
        import Queue as Q
        pq = Q.PriorityQueue()
        for l in lst:
            if l:
                pq.put(Node(iter(l)))
        while pq.empty():
            return ret
        curNode = pq.get()
        curVal = curNode.val
        nextVal = curVal
        while curVal == nextVal:
            nextVal = next(curNode.ite, None)
        if nextVal:
            curNode.val = nextVal # 这步注意一下，新的值要保存进node里面
            pq.put(curNode)
        while not pq.empty():
            curNode = pq.get()
            nextVal = curNode.val;
            if curVal == nextVal:
                count += 1
            else:
                if count >= k:
                    ret.append(curVal)
                count = 1
                curVal = nextVal
            while curVal == nextVal:
                nextVal = next(curNode.ite, None)
            if nextVal:
                curNode.val = nextVal
                pq.put(curNode)
        if count >= k:
            ret.append(curVal)
        return ret

l1 = [1,1,1,1,2,2,2,3,3,3,4,4,4,4,4,4,5,5,5,5]
l2 = [1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,4,4,4,4,4,5,5,5,5]
l3 = [1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3,3,3,4,4,4,5,5,5,5]
l4 = [1,1,1,1,3,3,3,3,3,5,5,5,5]
l5 = [1,1,1,1,1,1,2,2,2,2,3,3,3,3,5,5,5,5]
lst = [l1, l2, l3, l4, l5]
ktimes = KTimes()
print ktimes.ktimes(lst, 5)
