class GitCommit:
    def shortestPathToParent(self, parent, root1, root2):
        import Queue as Q
        import sys
        q = Q.Queue()
        minLen = sys.maxint
        minNode = None
        qMap = {}
        qMap[root1] = 0
        q.put(root1)
        while not q.empty():
            node = q.get()
            parent = node.parent
            for n in parent:
                n.length += node.length
                qMap[n] = n.length
                if n.parent:
                    q.put(n)
        q.put(root2)
        while not q.empty():
            node = q.get()
            for n in node.parent:
                n.length += node.length
                if n in qMap:
                    minLen = minLen if minLen < (n.length + qMap[n]) else n.length + qMap[n]
                    node = node if minLen < (n.length + qMap[n]) else n
        return minNode, minLen

class Node:
    def __init__(self):
        self.parent = []
        self.length = 0

n1 = Node();n2 = Node();n3 = Node();n4 = Node;
n4.parent = n3;n3.parent = n2;n2.parent = n1;
n4.index = 4;n3.index = 3; n2.index = 2; n1.index = 1
gc = GitCommit()
ret = gc.shortestPathToParent(n2, n3, n4)
