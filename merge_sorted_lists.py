# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        a=[]
        while list1:
            a.append(list1.val)
            list1=list1.next
        while list2:
            a.append(list2.val)
            list2=list2.next
        a.sort()
        print(a)
        head=ListNode(-1)
        t=head
        print(t)
        for x in range(len(a)):
            t.next= ListNode(a[x])
            t=t.next
        print(head)
        head=head.next
        print(head)
        return head