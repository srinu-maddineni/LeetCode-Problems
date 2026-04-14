/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

/**
 Do not return anything, modify head in-place instead.
 */
function reorderList(head: ListNode | null): void {
    if(!head ||!head.next){
        // return head
    }
    let curr = head
    let fast = curr
    let slow = curr

    while(fast.next && fast.next.next ){
        slow = slow.next
        fast=fast.next.next
 
    }

    let prev = null
    let curr1 = slow.next
    slow.next = null
    while(curr1){
        let node = curr1.next
        curr1.next = prev
        prev = curr1
        curr1 = node
    }
    while(prev && curr){
        let node1 = curr.next
        let node2 = prev.next
        curr.next = prev
        prev.next = node1
        curr=node1
        prev = node2

    }

    // return slow
};
