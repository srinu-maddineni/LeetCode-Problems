# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        if not head or  not head.next or k==0:
            return head
        t = head
        l = 1
        while t.next:
            t = t.next
            l+=1
        
        k = k % l
        if k ==0:
            return head
        curr = head
        for _ in range(l - k -1):
            curr = curr.next
        
        new_head = curr.next
        t.next = head
        curr.next = None
        return new_head


        

        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        
