# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        a, b = headA, headB
        while a != b:
            a = headB if a == None else a.next
            b = headA if b == None else b.next
        # 这里不用判断没有相交的原因是既然A与B互换了，每个指针都走了A+B个节点，所以最后一定都指向None（前提是没有cycle）
        return a
n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n6 = ListNode(6)
n7 = ListNode(7)
n1.next = n2
n2.next = n3

n4.next = n5
n5.next = n6
n6.next = n7

sol = Solution()
ret = sol.getIntersectionNode(n1, n4)
print ret.val if ret else ret
