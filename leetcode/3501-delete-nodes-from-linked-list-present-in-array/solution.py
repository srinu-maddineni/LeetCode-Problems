# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        # arr = []
        # curr = head
        # while curr:
        #     if curr.val in nums:
        #         curr = curr.next
        #     else:
        #         arr.append(curr.val)
        #         curr = curr.next
        # h = ListNode(0)
        # dummy = h
        # for i in arr:
        #     node = ListNode(i)
        #     dummy.next = node
        #     dummy = dummy.next
        # return h.next
        s = set(nums)
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        curr = head
        while curr:
            if curr.val in s:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return dummy.next
