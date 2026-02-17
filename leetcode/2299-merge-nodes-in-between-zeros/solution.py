# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return 0
        curr = head.next
        s =0
        dumy = ListNode(0)
        h = dumy
        while curr:
            if curr.val ==0:
                node = ListNode(s)
                dumy.next = node
                dumy = dumy.next
                s =0
            else:
                s+=curr.val
            curr = curr.next
        return h.next



        
