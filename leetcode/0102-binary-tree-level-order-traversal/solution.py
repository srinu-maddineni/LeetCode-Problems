# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        quee = deque([root])
        r = []
        while quee:
            length_level = len(quee)
            sol = []
            for i in range(length_level):
                node = quee.popleft()
                sol.append(node.val)
                if node.left:
                    quee.append(node.left)
                if node.right:
                    quee.append(node.right)
            r.append(sol[:])
        return r
        
