# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def doubleIt(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        curr = head
        res = ''
        
        while curr:
            res+=str(curr.val)
            curr = curr.next
        print(res)
        res = str(int(res)*2)
        print(res)
        dummy = ListNode(0)
        curr = dummy
        i=0
        while i<len(res):
            curr.next = ListNode(int(res[i]))
            i+=1
            curr = curr.next
        return dummy.next

        print(res)


        