/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {ListNode} head
 * @return {TreeNode}
 */
var sortedListToBST = function(head) {
    let arr = []

    let curr = head

    while(curr){
        arr.push(curr.val)
        curr = curr.next
    }
    console.log(arr)
    function binary(num){
        if(num.length === 0){
            return null
        }
        let mid = Math.floor(num.length/2)
        let root =new TreeNode(num[mid])
        root.left = binary(num.slice(0,mid))
        root.right = binary(num.slice(mid+1))
        return root
    }
    return binary(arr)
};
