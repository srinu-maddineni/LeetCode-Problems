from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        if not root:
            return []
        q = deque()
        q.append(root)
        arr = []
        i = 0
        k = i
        while q:
            l = len(q)
            s= []
            for i in range(l):
                node = q.popleft()
                s.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)

            
            arr.append(s[:])



        return arr

        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        
