# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        if not root:
            return True
        arr = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            arr.append(node.val)
            dfs(node.right)
        dfs(root)
        ar = arr[:]
        if ar == sorted(arr):
            k = len(set(ar))
            r = len(arr)
            if k == r :

                return True
            else: return False
        else:
            return False

        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        
