# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        dumy = ListNode(0)
        dumy.next = head
        curr = dumy
        while curr.next and curr.next.next:
            f =curr.next
            s = curr.next.next
            f.next = s.next
            s.next = f
            curr.next = s
            curr = curr.next.next
        return dumy.next
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
