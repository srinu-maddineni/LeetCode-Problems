/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

function convertBST(root: TreeNode | null): TreeNode | null {
    let sum =0
    let curr = root
    function dfs(curr){
        if(!curr) return
        if(curr.right) dfs(curr.right)
        sum+=curr.val
        curr.val = sum
        if(curr.left) dfs(curr.left)
    }
    dfs(curr)
    return root
};
