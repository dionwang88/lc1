# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        (1) Move: fast arrives the end, slow arrives the middle.
        1 -> 1 -> 2 -> 1 -> null
                  s          f
        (2) Reverse: reverse right half, slow is the 2nd head.
        1 -> 1    null <- 2 <- 1
        h                      s
        (3) Compare: run the two pointers head and slow and compare.
        1 -> 1    null <- 2 <- 1
             h            s
        In this example, since slow != null, return false.
        """
        if not head or not head.next:
            return True
        fast, slow = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        if fast:
            slow = slow.next

        slow = self.reverse(slow)
        while slow and head.val == slow.val:
            head = head.next
            slow = slow.next
        return slow == None

    def reverse(self, head):
        pre = None
        while head:
            nextNode = head.next
            head.next = pre
            pre = head
            head = nextNode
        return pre
