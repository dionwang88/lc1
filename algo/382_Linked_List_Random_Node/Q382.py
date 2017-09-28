# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head


    def getRandom(self):
        c = self.head
        r = c.val
        i = 1
        while c.next:
            c = c.next
            if self.randInt(0, i) == i:
                r = c.val
            i += 1
        return r

    def randInt(self, minVal, maxVal):
        from random import random
        return minVal + int(random() * (maxVal - minVal + 1))


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
