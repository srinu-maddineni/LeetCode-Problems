/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */

/**
 * @param {TreeNode} root
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {TreeNode}
 */
var lowestCommonAncestor = function(root, p, q) {
    // let min = root.val
    // let queue = [root]
    // let m = false
    // let n = false

    // while(queue.length>0){
    //     let node = queue.shift()
    //     min = Math.min(min,node.val)
    //     if(node === p) m = true
    //     if(node === q) n = true
    //     if(m && n){
    //         break
    //     }
    //     if(node.left) queue.push(node.left)
    //     if(node.right) queue.push(node.right)
    // }
    // return min
    while(root){
        if(p.val <root.val && q.val<root.val){
            root = root.left
        }
         else if (p.val > root.val && q.val > root.val) {
            root = root.right;
        } 
        else{
            return root
        }}
};