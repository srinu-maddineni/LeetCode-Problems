/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {number[][]} descriptions
 * @return {TreeNode}
 */
var createBinaryTree = function(descriptions) {
    let map = new Map()
    let childern = new Set()
    for(let i of descriptions){


        if(!map.has(i[0])){
           map.set(i[0],new TreeNode(i[0]))
        }
        if(!map.has(i[1])){
           map.set(i[1],new TreeNode(i[1]))
        }
        let par = map.get(i[0])
        let child = map.get(i[1])
        if(i[2] === 1){
            par.left = child
        }
        else{
            par.right = child
        }
        childern.add(i[1])
    }
    for(let i of descriptions){
        if(!childern.has(i[0])){
            return map.get(i[0])
        }
    }
};
