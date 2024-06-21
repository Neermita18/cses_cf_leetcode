# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # node=None
        
        # while head:
        #     t= head.next
        #     head.next=node
        #     node=head
        #     head=t
        # head=node
        # print(head)
        # c= head
        # if :
        #     c=None
        # if n==1:
        #     if c.next and c.next.next:
        #         c.next=c.next.next
        #     else:
        #         c.next=None

        # i=1
        # while c.next:
        
        #     if i==n-1:
        #         break
        #     i+=1
        #     c=c.next
            
        # if c.next and c.next.next:
        #     c.next=c.next.next
        # else:
        #     c.next=None
        # print(head)
        c= head
        i=1
        while c.next:
            c=c.next
            i+=1
        print(i)
        s= i-n
        print(head)
        c= head
        if i==1:
            return None
        if i==n:
            head=head.next
        j=1
        while c:
            
            if j==s:
                c.next=c.next.next
            j+=1
            c=c.next
           
        return head
