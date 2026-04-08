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

function getDecimalValue(head: ListNode | null): number {
    let n = []

    while(head){
        n.push(head.val)
        head = head.next
    }
    let res = 0
    let k =0
    for(let i =n.length-1;i>=0;i--){
        res+=(2**k)*n[i]
        k++
    }
    console.log(n)
    return res
};
