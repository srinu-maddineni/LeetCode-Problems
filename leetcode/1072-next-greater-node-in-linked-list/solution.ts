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

function nextLargerNodes(head: ListNode | null): number[] {
    let curr = head

    let arr = []
    while(curr){
        let curr1 = curr.next
        while(curr1){
            if(curr1.val>curr.val){
                arr.push(curr1.val)
                break
            }
            else{
                curr1 = curr1.next
            }
        }
        if(curr1 === null) arr.push(0)
        curr = curr.next
    }
    return arr
};
