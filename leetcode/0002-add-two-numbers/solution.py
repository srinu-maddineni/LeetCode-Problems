# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        i =1
        j =1
        curr1 = l1
        curr2 = l2
        n = 0
        m=0
        while curr1:
            n+=curr1.val*i
            curr1 = curr1.next
            i *=10
        while curr2:
            n+=curr2.val*j
            curr2 = curr2.next
            j*=10

        print(n+m)
        k = str(n+m)[::-1]
        l3 =ListNode()
        curr = l3
        for s in k:
            curr.next = ListNode(int(s))
            curr = curr.next
        return l3.next
        

        
        

        
        

        return l3




 

        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
