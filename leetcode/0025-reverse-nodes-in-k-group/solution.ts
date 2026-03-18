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

function reverseKGroup(head: ListNode | null, k: number): ListNode | null {
    let dummy = new ListNode(0,head)
    let prev = dummy
    let curr = dummy.next
    while(curr != null){
        let tail = curr
        let count = 0
        while(curr != null && count<k){
            curr = curr.next
            count+=1
            
        }
        if(count<k){
            prev.next=tail
            
        }
        else{
           prev.next = reverse(tail,k)
           prev = tail
        }
    }
 return dummy.next
};
function reverse(currList:ListNode,k:number){
   let prev = null
   let curr = currList
   let count=0
   while(curr != null && count < k){
    
    let node = curr.next
    curr.next=prev
    prev = curr
    curr = node
    count +=1
   }
   return prev
}
