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
        # c= head
        # a=[]
        
        # while c:
        #     a.append(c)
        #     c=c.next
        # n= a[0]
        # tail=None
        # # print(a)
        # for i in range(len(a)//2):
        #     a[i].next= a[-1-i]
        #     a[i].next.next= a[i+1]
        #     tail= a[i].next.next
        # if tail:
        #     tail.next=None
        # head=n
        # print(head)
        slow=head
        fast= head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        second= slow.next
        node = None
        slow.next=None
        while second:
            t= second.next
            second.next=node
            node=second
            second=t

        second=node
        first=head
        while second:
            t1=first.next
            t2= second.next
            first.next= second
            second.next=t1
            first=t1
            second=t2