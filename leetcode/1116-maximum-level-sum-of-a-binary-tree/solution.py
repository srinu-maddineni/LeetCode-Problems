# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return
        quee = deque([root])
        level = 1
        max_sum_level = root.val
        cur =0
        while quee:
            length_quee = len(quee)
            level_sum =0
            for i in range(length_quee):
                node=quee.popleft()
                level_sum +=node.val
                if node.left:
                    quee.append(node.left)

                if node.right:
                    quee.append(node.right)
            cur+=1
            if level_sum > max_sum_level:
                level = cur
                max_sum_level = level_sum
        return level




        
