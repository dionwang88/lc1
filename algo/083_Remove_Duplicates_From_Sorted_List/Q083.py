# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        pre, cur = head, head
        while cur:
            while cur.next and cur.val == cur.next.val:
                cur = cur.next
            cur = cur.next
            pre.next = cur
            pre = cur
        return head
