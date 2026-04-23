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

function findBottomLeftValue(root: TreeNode | null): number {
    if(!root){
        return 0
    }
    let queue = [root]
    let res = []
    while(queue.length>0){
        let l = queue.length
        let arr = []
        for(let i =0;i<l;i++){
            let node = queue.shift()
            
            arr.push(node.val)
            if(node.left) queue.push(node.left)
            if(node.right) queue.push(node.right)

        }
        res.push(arr)
        
    }
    return res[res.length-1][0]
};
