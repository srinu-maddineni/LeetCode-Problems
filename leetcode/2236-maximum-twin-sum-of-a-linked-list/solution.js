/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {number}
 */
var pairSum = function(head) {
    if(!head || !head.next){
        return 0
    }
    
    let curr = head
    let slow = head
    let prev = null
    while(curr && curr.next){
        prev = slow
        slow = slow.next
        curr=curr.next.next
        
    }

    prev = null
    let p = null
    while(slow){
        let temp = slow.next
        slow.next = p
        p=slow
        slow = temp
    }

    curr = head
    console.log(p,curr)
    let maxSum = 0
    while(curr && p){
        maxSum = Math.max(maxSum,(curr.val+p.val))
        curr=curr.next
        p = p.next
    }

    return maxSum
};
