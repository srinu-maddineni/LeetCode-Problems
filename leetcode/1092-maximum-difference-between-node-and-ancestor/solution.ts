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

function maxAncestorDiff(root: TreeNode | null): number {
    if(!root){
        return 0
    }
    let v = 0
    let m = []
    function dfs(root,max,min){
        if(!root) {
            return max - min
        }
        min = Math.min(min,root.val)
        max = Math.max(max,root.val)
        let left = dfs(root.left,max,min)
        let right = dfs(root.right,max,min)
        return Math.max(left,right)
    }
    
    return dfs(root,root.val,root.val)
};
