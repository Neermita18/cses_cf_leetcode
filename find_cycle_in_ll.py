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
        c=head
        d=set()
        while c:
            if c in d:
                return True
            d.add(c)
            c=c.next
        return False