# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        if head == None:
            return head
        duplicate = ListNode(0)
        duplicate.next = head 
        curr = duplicate
       
        
        while curr.next:

            if curr.next.val == val:
                curr.next = curr.next.next
                
            else:
                curr = curr.next
              
        return duplicate.next
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        
