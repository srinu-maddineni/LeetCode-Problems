# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        quee = deque([root])
        depth = 1
        while quee:
            length_of_quee = len(quee)
            for i in range(length_of_quee):
                node = quee.popleft()
                if node.left: quee.append(node.left)
                if node.right: quee.append(node.right)
                if not node.left and not node.right: return depth
            depth +=1

        
