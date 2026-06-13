/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function(nums) {
    let maxSum = nums[0]
    let curr = 0
    for(let num of nums){
        curr+=num
        maxSum = Math.max(curr,maxSum)
        if(curr<0){
            curr = 0
        }

    }
    return maxSum
    
};
