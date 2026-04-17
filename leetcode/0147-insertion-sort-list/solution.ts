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

function insertionSortList(head: ListNode | null): ListNode | null {
    if(!head) return
    let curr = head
    let arr = []
    while(curr){
        arr.push(curr.val)
        curr = curr.next
    }
    arr.sort((a,b)=>a-b)
    let curr1 = new ListNode(0)
    let h = curr1
    for(let i=0;i<arr.length;i++){
        let c =new ListNode(arr[i])
        curr1.next  = c
        curr1=curr1.next
    }
    return h.next
};
