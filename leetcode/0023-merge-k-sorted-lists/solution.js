/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode[]} lists
 * @return {ListNode}
 */
var mergeKLists = function(lists) {
    let dummy =new ListNode(0)
    // let curr = dummy

    let arr = []
    for(let i= 0;i<lists.length;i++){
        let curr = lists[i]
        while(curr){
            arr.push(curr.val)
            curr = curr.next
        }
    }
    arr.sort((a,b)=>a-b)
    let c = dummy
    for(let i=0;i<arr.length;i++){
        c.next =new ListNode(arr[i])
         
        c=c.next
    }
    return dummy.next
};
