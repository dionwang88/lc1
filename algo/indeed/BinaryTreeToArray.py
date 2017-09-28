class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.index = -1

class BinaryTreeToArray:
    def treeToArray(self, root):
        import Queue as Q
        if not root:
            return []
        '''
        用nMap来记录节点index和value
        '''
        nMap, q = {}, Q.Queue()
        root.index = 0
        q.put(root)
        nMap[0] = root.val
        while not q.empty():
            node = q.get()
            left, right = node.left, node.right
            if left:
                left.index = 2 * node.index + 1
                nMap[left.index] = left.val
                q.put(left)
            if right:
                right.index = 2 * node.index + 2
                nMap[right.index] = right.val
                q.put(right)

        ret = [None for _ in xrange((sorted(nMap)[-1] + 1))]
        for key in sorted(nMap):
            ret[key] = nMap[key]
        return ret

root = Node(0);
n1 = Node(1);n2 = Node(2);
n3 = Node(3);n4 = Node(4);
n5 = Node(5);n6 = Node(6);
n7 = Node(17);n8 = Node(8);
n9 = Node(9);n10 = Node(10);
n11 = Node(11);n12 = Node(12);
root.left = n1;root.right = n2;
n1.left = n3;n1.right = n4;
n2.left = n5;
n3.left = n7
n4.left = n9;n4.right = n10;

bta = BinaryTreeToArray()
print bta.treeToArray(root)
