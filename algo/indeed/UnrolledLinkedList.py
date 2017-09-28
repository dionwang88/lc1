class Node:
    def __init__(self):
        self.chars = [None] * 5
        self.charLen = 0
        self.next = None

class LinkedList:
    def __init__(self, node):
        self.head = node
        self.totalLen = 0

    def printList(self):
        node = self.head
        while node:
            for c in node.chars:
                print c,
            node = node.next

    def get(self, index):
        if index >= self.totalLen:
            return
        node = self.head
        while index > node.charLen and node:
            index = index - node.charLen
            node = node.next
        return node.chars[index-1]

    def insert(self, char, index):
        node = self.head
        Length = len(node.chars)
        while index >= Length:
            if node.next:
                index = index - Length
                node = node.next
            else:
                temp = Node()
                node.next = temp
                node = temp
                index = index - Length
        if node.charLen == 0: # 插入进一个新节点
            node.chars[index-1] = char
            node.charLen = 1
        if node.charLen < Length - 1: # 当前节点还有空位
            chars = node.chars
            i = Length - 1
            while i != index - 1:
                chars[i] = chars[i - 1]
                i = i - 1
            chars[index - 1] = char
            node.chars = chars
            node.charLen += 1
        elif node.charLen == Length -1 :# 当前节点没有空位了，需要再创建一个新节点，并依次挪开
            nodeNext = node.next;
            temp = Node()
            node.next = temp
            temp.next = nodeNext
            temp.chars[0] = node.chars[Length - 1]
            temp.charLen = 1
            i = Length - 1
            while i > index - 1:
                node.chars[i] = node.chars[i - 1]
                i = i - 1
            node.chars[i] = char

head = Node()
head.chars = ['a','b','c','','']
head.charLen = 3
node1 = Node()
node1.chars = ['f','g','h','i','']
node1.charLen = 4
node2 = Node()
node2.chars = ['l','m','','','']
node2.charLen = 2
head.next = node1
node1.next = node2
ll = LinkedList(head)
ll.totalLen = 9
ll.insert('19', 12)
ll.printList()
