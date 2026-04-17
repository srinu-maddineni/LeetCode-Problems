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

function addTwoNumbers(l1: ListNode | null, l2: ListNode | null): ListNode | null {

    function reverse(l:ListNode|null){
        let prev = null
        if(!l) return l

        let curr = l
        

        while(curr){
            let newNode = curr.next
            curr.next = prev
            prev = curr
            curr = newNode 
  
        }
        return prev
    }
    let lr1= reverse(l1)
    let lr2 = reverse(l2)

    let dummy =new ListNode(0)
    let k = dummy
    let carry = 0
 
        while(lr1 || lr2 ||carry){
            let sum =carry
            if(lr1){
                sum+=lr1.val
                lr1= lr1.next
            }
            if(lr2){
                sum+=lr2.val
                lr2=lr2.next
            }
            let r = sum%10
            carry = Math.floor(sum/10)
            let temp = new ListNode(r)
            k.next = temp
            k = k.next
        }
    

    return reverse(dummy.next)
};
