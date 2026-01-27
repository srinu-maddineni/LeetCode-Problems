"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        que = deque([root])
        while que:
            n = len(que)
            prev = None
            for _ in range(n):
                q = que.popleft()
                if prev:
                    prev.next =q
                prev = q
                if q.left:que.append(q.left)
                if q.right:que.append(q.right)

            prev.next=None
        return root
                
        
