# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        my_head = ListNode(0)
        my_head.next = head
        cur = head.next
        while cur:
            temp = cur.next
            cur.next = my_head.next
            my_head.next = cur
            cur = temp
        head.next = None
        return my_head.next
