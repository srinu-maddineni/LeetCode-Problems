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

function levelOrderBottom(root: TreeNode | null): number[][] {
    if(!root){
        return []
    }
    let queue = [root]
    let res = []
    while(queue.length>0){
        let k = queue.length
        let curr = []
        for(let i=0;i<k;i++ ){
            let node = queue.shift()!
            curr.push(node.val)
            if(node.left) queue.push(node.left)
            if(node.right) queue.push(node.right)

        }
        res.push(curr)
    }
    console.log(res)
    return [...res].reverse()
};
