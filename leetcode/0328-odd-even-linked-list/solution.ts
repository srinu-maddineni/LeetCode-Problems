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

function oddEvenList(head: ListNode | null): ListNode | null {
    let curr = head 
    let od =new ListNode(0)
    let o = od
    let ev =new ListNode(0)
    let e = ev
    let i =1
    while(curr){
        if(i%2 !=0){
            od.next=curr
            od = od.next
        }
        else{
            ev.next = curr
            ev=ev.next
        }
        i++
        curr = curr.next
    }
    ev.next =null
    od.next =e.next
    return o.next
};
