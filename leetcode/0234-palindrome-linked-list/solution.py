# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        curr = head
        a = []
        while curr:
            a.append(curr.val)
            curr = curr.next
        print(a)
        if a == a[::-1]:
            return True
        else:
            return False
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        
