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

function kthSmallest(root: TreeNode | null, k: number): number {
    if(!root){
        return 
    }
    let result = []
    dfs(root,result)
    return result[k-1]
};
function dfs(root,result){
    if(!root) return 
    dfs(root.left,result)
    result.push(root.val)
    dfs(root.right,result)
    return result

}
