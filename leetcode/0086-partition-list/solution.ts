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

function partition(head: ListNode | null, x: number): ListNode | null {
    if(!head) return null

    let left =new ListNode(0)
    let right = new ListNode(0)
    let rel = left
    let j = right
    let curr = head
    while(curr){

        if(curr.val<x){
            left.next = curr
            left = left.next
            curr= curr.next
        }
        else{
            right.next = curr
            right = right.next
            curr = curr.next
        }
    }
    right.next = null
    left.next = j.next
    return rel.next
};
