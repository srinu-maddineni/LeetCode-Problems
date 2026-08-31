# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """
        if not head or not head.next:
            return [-1,-1]
        critical = []
        prev = head
        curr = head.next
        i=2
        mi = float('inf')
        last =0
        first =0
        while curr.next:
            if (curr.val>prev.val and curr.val>curr.next.val) or (curr.val<prev.val and curr.val<curr.next.val):
                if first== 0:
                    first = i
                if last !=0:
                    mi = min(mi,i-last)
                    last = i
                else:
                    last = i
                 
                # critical.append(i)
            i+=1
            curr=curr.next
            prev=prev.next
        # if len(critical)<2:
        #     return [-1,-1]
        # mi = float('inf')
        # for i in range(1,len(critical)):
        #     mi = min(mi,critical[i]-critical[i-1])
        # print(mi)
        # return [mi,critical[-1]-critical[0]]
        print(mi)
        if mi == float('inf'):
            return [-1,-1]
        return [mi,last-first]


        