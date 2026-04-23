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

function isUnivalTree(root: TreeNode | null): boolean {
    if(!root){
        return false
    }
    let n = root.val
    function dfs(root){
        if(!root) return true
        if(root.val != n){
            return false
        }
        console.log(root.val)
       
        return  dfs(root.left) && dfs(root.right)

    }

    return dfs(root)
};
