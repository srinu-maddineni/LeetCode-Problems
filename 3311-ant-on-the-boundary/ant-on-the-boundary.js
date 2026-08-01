/**
 * @param {number[]} nums
 * @return {number}
 */
var returnToBoundaryCount = function(nums) {
    let n = 0
    let result = -1
    for(let i=0;i<nums.length;i++){
        if(n === 0){
            result++
        }
        n+=nums[i]
    }
    if(n===0) result++
    return result
};