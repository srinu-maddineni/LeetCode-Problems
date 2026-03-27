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

function preorderTraversal(root: TreeNode | null): number[] {
    if(!root) return []
    let result = []
    return pst(root,result)
};
function pst(root,result){
    if(!root) return 
    result.push(root.val)
    if(root.left) pst(root.left,result)
    if(root.right) pst(root.right,result)
    return result
}
