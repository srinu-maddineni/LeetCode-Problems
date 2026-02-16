# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stk = [root]
        c = 0
        while stk:
            node = stk.pop()
            c+=1
            if node.right: stk.append(node.right)
            if node.left: stk.append(node.left)
        return c

                    
        
