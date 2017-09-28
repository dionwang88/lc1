# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None or head.next == None:
            return False

        fast, slow = head, head
        while fast:
            if fast.next:
                fast = fast.next.next
                slow = slow.next
            else:
                return False
            if fast == slow:
                return True
        return False
