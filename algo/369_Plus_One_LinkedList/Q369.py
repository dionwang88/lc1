class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def plusOne(self, head):
        '''
        可以做的就是先把链表翻转一下，然后现在就是链尾是高位了，我们进行加1处理运算结束后，再把链表翻转回来即可
        '''
        if not head:
            return head
        fakeHead = ListNode(-1)
        fakeHead.next = head
        self.reverse(fakeHead)
        cur, pre = fakeHead.next, fakeHead
        val = cur.val + 1
        accu = 0
        while cur:
            if val + accu > 9:
                accu = 1
                cur.val = (cur.val + accu) % 10
            else:
                cur.val += accu
                accu = 0
            pre = cur
            cur = cur.next
            if cur:
                val = cur.val
        if accu > 0:
            cur = ListNode(accu)
            pre.next = cur
        self.reverse(fakeHead)

        return fakeHead.next

    def reverse(self, fakeHead):
        prev, cur = fakeHead.next, fakeHead.next.next
        while cur:
            temp = cur.next
            head = fakeHead.next
            fakeHead.next = cur
            cur.next = head
            prev.next = temp
            cur = temp


sol = Solution()
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(9)
node1.next = node2
node2.next = node3
node3.next = node4

node = sol.plusOne(node1)
while node:
    print node.val
    node = node.next
