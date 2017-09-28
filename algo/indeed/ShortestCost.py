class Node:
    def __init__(self, number):
        self.edges = []
        self.number = number

class Edge:
    def __init__(self, node, cost):
        self.node = node
        self.cost = cost

class Test:
    def getShortestCostNode(self, root):
        '''
        stack: 用来保存节点的边
        visited: 用来保存该节点是否visited
        retMap: 包含从root到所有的叶节点的cost map
        costs：记录从root到所有非叶节点的cost值
        '''
        import sys
        if not root or not root.edges:
            return
        stack, visited, retMap, costs = [], {}, {}, {}
        count, minValue, ret = 0, -sys.maxint, None
        for edge in root.edges:
            stack.append(edge)
            costs[edge.node] = edge.cost
        while stack:
            edge = stack.pop()
            node = edge.node
            if node in visited:
                continue
            count = costs[node]
            visited[node] = True
            if node.edges:
                for edge1 in node.edges:
                    if edge1.node not in visited:
                        stack.append(edge1)
                        costs[edge1.node] = count + edge1.cost
            else:
                retMap[node] = count
        return sorted(retMap.values())[0]

root = Node(0)
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
edge1 = Edge(node1, 2)
edge2 = Edge(node2, 3)
edge3 = Edge(node3, 1)
edge4 = Edge(node4, 4)
edge5 = Edge(node5, 6)
edge6 = Edge(node6, 2)
root.edges = [edge1, edge2]
node1.edges = [edge3, edge5]
node2.edges = [edge4]
node4.edges = [edge6]

test = Test()
test.getShortestCostNode(root)


import Queue as Q

q = Q.PriorityQueue()
q.put((-10,'ten'))
q.put((-1,'one'))
q.put((-5,'five'))
print q.qsize()
while not q.empty():
    print q.get(),
