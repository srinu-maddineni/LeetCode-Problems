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

function bstToGst(root: TreeNode | null): TreeNode | null {
    let sum = 0
    let curr = root
    function dfs(root){
        if(!root) return
        if(root.right){
            dfs(root.right)
        }
        sum+=root.val
        root.val = sum
        if(root.left){
            dfs(root.left)
        }
    }
    dfs(curr)
    return root
};
