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

function findTarget(root: TreeNode | null, k: number): boolean {
    if(!root) return
    let m = new Set()
    function dfs(root){
        if(!root) return false
        let target = k - root.val
        if(m.has(root.val)){
            return true
        }
        else{
            m.add(target)
        }
        return dfs(root.left) || dfs(root.right)

    }
    return dfs(root)?true:false
};
