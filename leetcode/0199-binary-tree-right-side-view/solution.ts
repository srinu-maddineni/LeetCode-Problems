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

function rightSideView(root: TreeNode | null): number[] {
    if(!root){
        return []
    }
   let queue = [root]
    let result:number [] = []
    while(queue.length>0){
         let size =queue.length
        for(let i=0;i<size;i++ ){
             let curr = queue.shift()
             if(i == size-1) result.push(curr.val)
             if(curr.left) queue.push(curr.left)
             if(curr.right) queue.push(curr.right)
        }

    }
  return result
};


