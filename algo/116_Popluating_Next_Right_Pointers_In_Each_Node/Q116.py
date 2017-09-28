# Definition for binary tree with next pointer.
# class TreeLinkNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
import Queue as Q

class Solution(object):
    def connect(self, root):
        if not root:
            return
        queue = Q.Queue()
        queue.put(root)
        while queue.qsize() > 0:
            size = queue.qsize()
            prev = None
            node = None
            while size > 0:
                node = queue.get()
                if prev:
                    prev.next = node
                prev = node
                if node.left:
                    queue.put(node.left)
                if node.right:
                    queue.put(node.right)
                size -= 1
            node.next = None

    def connect1(self, root):
        if not root:
            return
        prev, cur = root, None
        while prev.left:
            cur = prev
            while cur:
                cur.left.next = cur.right
                if cur.next:
                    cur.right.next = cur.next.left
                    cur = cur.next
            prev = prev.left
