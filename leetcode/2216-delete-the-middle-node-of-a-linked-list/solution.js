/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var deleteMiddle = function(head) {
    if(!head || !head.next){
        return null
    }
    let curr = head
    let slow = head
    let prev = null
    while(curr && curr.next){
        prev = slow
        slow = slow.next
        curr = curr.next.next
    }
    prev.next = slow.next
    return head

};
