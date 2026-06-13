/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
    let n = 0
    let cand = null
    for(let num of nums){
        if(n===0){
            cand = num
        }
        n+=(cand===num)?1:-1
    }
    return cand
};
