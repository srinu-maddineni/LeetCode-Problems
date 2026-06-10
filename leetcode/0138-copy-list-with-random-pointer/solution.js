/**
 * // Definition for a _Node.
 * function _Node(val, next, random) {
 *    this.val = val;
 *    this.next = next;
 *    this.random = random;
 * };
 */

/**
 * @param {_Node} head
 * @return {_Node}
 */
var copyRandomList = function(head) {

        if(!head){
            return head
    }

    let curr = head

    while(curr){
        let newNode = new _Node(curr.val,curr.next,curr.random)
        let temp = curr.next
        curr.next = newNode
        newNode.next = temp
        curr = newNode.next

    }
     curr = head
     let dummy = new _Node(0)
     let c = dummy
     while(curr){
        if(curr.random){
            curr.next.random = curr.random.next
        }
        curr = curr.next.next
     }
     curr = head
     while(curr){
        let m = curr.next.next
        c.next = curr.next
        c= c.next
        curr.next = m
        curr = m
     }
    return dummy.next
    
};
