# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
      
        c = 0
        curr =  head
        while curr:
            c+=1
            curr = curr.next
        if c == n:
            return head.next
        curr = head
        for i in range(c -n-1):
            curr = curr.next
        if curr.next:
            curr.next = curr.next.next
        return head


        print(m)
        
        



        
        
        # print(curr.val)
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        
