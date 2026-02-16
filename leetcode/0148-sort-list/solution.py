# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head :
            return head
        curr = head
        arr =[]
        while curr:
            arr.append(curr.val)
            curr = curr.next
        arr.sort()
        m = ListNode(0)
        curr = m
        for i in range(len(arr)):
            node = ListNode(arr[i])
            curr.next = node
            curr = curr.next
        return m.next


        

        
