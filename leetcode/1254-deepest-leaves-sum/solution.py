# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root :
            return
        q = deque([root])
        while q:
            level_sum = 0        
            for i in range(len(q)):
                k = q.popleft()
                level_sum+=k.val
                if k.left:q.append(k.left)
                if k.right:q.append(k.right)
            
        return level_sum





        
