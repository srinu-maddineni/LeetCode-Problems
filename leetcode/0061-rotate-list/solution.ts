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

function rotateRight(head: ListNode | null, k: number): ListNode | null {
    if(!head || !head.next || k==0){
        return head
    }

    let curr = head
    let len = 1
    while(curr.next){
        len++
        curr = curr.next
    }
    k = k%len
    if(k===0){
        return head
    }
    let cur = head
    for(let l =0;l<len-k-1;l++){
        cur = cur.next
    }
    let newHead = cur.next
    curr.next = head
    cur.next= null

    return newHead
};
