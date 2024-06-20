# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        c= head
        a=[]
        
        while c:
            a.append(c)
            c=c.next
        n= a[0]
        tail=None
        # print(a)
        for i in range(len(a)//2):
            a[i].next= a[-1-i]
            a[i].next.next= a[i+1]
            tail= a[i].next.next
        if tail:
            tail.next=None
        head=n
        # print(head)