# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        res = []
        def inorder(root):
            if not root:
                return 
            if root.left: inorder(root.left)
            res.append(root.val)
            if root.right:inorder(root.right)
            return res
        inorder(root)
        
        def blance(res):
            if not res:
                return None
            m =len(res)//2
            node = TreeNode(res[m])
            node.left = blance(res[:m])
            node.right = blance(res[m+1:])
            return node
        return blance(res)



        
