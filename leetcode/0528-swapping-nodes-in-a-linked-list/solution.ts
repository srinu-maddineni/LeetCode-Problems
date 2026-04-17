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

function swapNodes(head: ListNode | null, k: number): ListNode | null {
    let slow = head
    let arr = []
    let n =0
    while(slow){
        arr.push(slow.val)
        slow = slow.next
    }
    [arr[k-1],arr[arr.length-k]] =[arr[arr.length-k],arr[k-1]]
    let rel = new ListNode(0)
    let r = rel
    for(let i =0;i<arr.length;i++){
        let m = new ListNode(arr[i])
        r.next = m
        r = r.next

    }
    console.log(arr)
    return rel.next
};
