# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        这里注意[1,1,2,2]这种情况
        """
        if not head or not head.next:
            return head
        allHead = ListNode(-1)
        allHead.next = head
        pre, cur = allHead, head
        while cur:
            while cur.next and cur.val == cur.next.val:
                cur = cur.next
            if pre.next == cur: # 没有重复的
                pre = pre.next
            else: # 有重复的，直接跳过
                pre.next = cur.next
            cur = cur.next # 最后把当前的设置为next

        return allHead.next

head = ListNode(1)
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(2)
head.next = node1
node1.next = node2
node2.next = node3
sol = Solution()
sol.deleteDuplicates(head)
