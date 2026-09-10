# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        ans = 0
        def post(root):
            nonlocal ans
            if not root:
                return 0,0
            l,cl =post(root.left)
            r,cr = post(root.right)
            s = root.val+l+r
            c = 1+cl+cr
            if s//c ==root.val:
                ans+=1

            return s,c
        # print(post(root))

        # queue = [root]
        # ans =0
        # while queue:
        #     node = queue.pop()
        #     k ,n= post(node)
        #     if (k//n) == node.val:
        #         ans+=1
        #     if node.left:queue.append(node.left)
        #     if node.right:queue.append(node.right)
        post(root)
        return ans


        