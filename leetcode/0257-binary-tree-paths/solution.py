# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        result = []
        def dfs(root,path):
            if not root:
                return
            if path :
                path+="->"+str(root.val)
            else:
                path=str(root.val)
            if not root.left and not root.right:
                result.append(path)
                return
            dfs(root.left,path)
            dfs(root.right,path)
        dfs(root,"") 
        return result

        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """
        
