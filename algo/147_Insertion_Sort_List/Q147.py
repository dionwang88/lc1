class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        allHead, newNode = ListNode(-1), ListNode(head.val)
        allHead.next, node = newNode, head.next
        while node:
            newNode = ListNode(node.val)
            temp = allHead.next
            pre = allHead
            while temp:
                if temp.val > newNode.val:
                    pre.next = newNode
                    newNode.next = temp
                    break
                else:
                    pre = temp
                temp = temp.next
            if pre.val < newNode.val:
                pre.next = newNode
            node = node.next
        return allHead.next


sol = Solution()
head = ListNode(0)
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
head.next = node2
node2.next = node1
node1.next = node4
node4.next = node5
node5.next = node3

# node = head
# while node:
#     print node.val,
#     node = node.next

ret = sol.insertionSortList(head)
while ret:
    print ret.val,
    ret = ret.next
