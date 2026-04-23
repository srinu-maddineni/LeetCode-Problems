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

function zigzagLevelOrder(root: TreeNode | null): number[][] {
    if(!root){
        return []
    }
    let queue = [root]
    let res = []
    let i=0
    while(queue.length>0){
        let l = queue.length
        let curr = []
        for(let i=0;i<l;i++){
            let node = queue.shift()
            curr.push(node.val)
            if(node.left) queue.push(node.left)
            if(node.right) queue.push(node.right)

        }
        if(i%2 ==0){
            res.push(curr)
        }
        else{

            res.push(curr.reverse())
        }

        i++
    }
    return res
};
