# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        这个解法很好,要多体会
        在做链表的题目时, 有时可以考虑使用这种方式来做
        """
        if not head or not head.next:
            return head

        hd1 = p1 = ListNode(0)
        hd2 = p2 = ListNode(0)
        while head:
            if head.val < x:
                p1.next = head
                p1 = p1.next
            else:
                p2.next = head
                p2 = p2.next
            head = head.next

        p2.next = None
        p1.next = hd2.next
        return hd1.next

node1 = ListNode(1)
node2 = ListNode(4)
node3 = ListNode(3)
node4 = ListNode(2)
node5 = ListNode(5)
node6 = ListNode(2)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

sol = Solution()
sol.partition(node1, 3)
