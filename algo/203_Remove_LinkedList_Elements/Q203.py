# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return head

        fakeNode = ListNode(-1)
        fakeNode.next = head
        prev, cur, nextNode = fakeNode, head, head
        while cur:
            while cur and cur.val == val:
                cur = cur.next
            if not cur:
                prev.next = cur
                break
            else:
                prev.next = cur
                prev = cur
                cur = cur.next
        return fakeNode.next
