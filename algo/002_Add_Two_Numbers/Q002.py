# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(-1)
        cur = head
        residual = 0
        while(l1!=None and l2!=None):
            sum = l1.val + l2.val + residual
            ln = ListNode(sum % 10)
            cur.next = ln
            residual = sum / 10
            l1 = l1.next
            l2 = l2.next
            cur = cur.next
        while(l1!=None):
            sum = l1.val + residual
            ln = ListNode(sum % 10)
            cur.next = ln
            residual = sum / 10
            cur = cur.next
            l1 = l1.next
        while(l2!=None):
            sum = l2.val + residual
            ln = ListNode(sum % 10)
            cur.next = ln
            residual = sum / 10
            cur = cur.next
            l2 = l2.next
        if(residual > 0):
            ln = ListNode(1)
            cur.next = ln
        return head.next


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
