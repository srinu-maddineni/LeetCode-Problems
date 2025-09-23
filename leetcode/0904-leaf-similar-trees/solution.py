# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        def leaf_node(root):
            a =[]
            stk = [root]
            while stk:
                node = stk.pop()
                if not node.right and not node.left:
                    a.append(node.val)
                if node.right: stk.append(node.right)
                if node.left: stk.append(node.left)
            return a


        r1 = leaf_node(root1)
        r2 = leaf_node(root2)
        if r1 == r2: return True
        else: return False


        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: bool
        """
        
