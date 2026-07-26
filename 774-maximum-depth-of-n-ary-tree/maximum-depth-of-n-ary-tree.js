/**
 * // Definition for a _Node.
 * function _Node(val,children) {
 *    this.val = val === undefined ? null : val;
 *    this.children = children === undefined ? null : children;
 * };
 */

/**
 * @param {_Node|null} root
 * @return {number}
 */
var maxDepth = function(root) {
    // console.log(root.children)
    if (!root) return 0
    
    let queue =[root]
    let depth =0
    while(queue.length>0){
        let n = queue.length
        depth++

        for(let i=0;i<n;i++){

            let node = queue.shift()
            for(let ch of node.children){
                queue.push(ch)
            }
        }
        console.log('//////')
    }
    return depth
};