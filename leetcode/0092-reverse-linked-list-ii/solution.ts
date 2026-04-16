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

function reverseBetween(head: ListNode | null, left: number, right: number): ListNode | null {
    if(!head) return null
    let i =1
    let dummy = new ListNode(0,head)
    let prev = dummy
    for(let i=1;i<left;i++){
        prev = prev.next
    }
    let curr = prev.next

        for(let i=0;i<right-left;i++){
            let newNode = curr.next
            curr.next = newNode.next
            newNode.next = prev.next
            prev.next = newNode
        }
        

    return dummy.next
};
