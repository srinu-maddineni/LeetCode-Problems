# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        if head == None:
            return False
        if head.next == None :
            return False
        f = head
        s = head
        while f and f.next:
            
            f = f.next.next
            s = s.next
            if s == f: return True
        return False
        """
        :type head: ListNode
        :rtype: bool
        """
        
