/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function(nums) {
    let l =0
    let s = new Set(nums)
    for(let num of s){
        if(!s.has(num-1)){
            let curr = num
            let currstk = 1
            while(s.has(curr+1)){
                curr=curr+1
                currstk++
            }
            l = Math.max(currstk,l)
        }
       
    }
    return l
};
