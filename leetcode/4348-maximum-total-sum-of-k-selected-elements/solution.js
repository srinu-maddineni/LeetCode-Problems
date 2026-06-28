/**
 * @param {number[]} nums
 * @param {number} k
 * @param {number} mul
 * @return {number}
 */
var maxSum = function(nums, k, mul) {
    nums.sort((a,b)=>b-a)
    let ans = 0
    for(let i=0;i<k;i++){
        let op1 = nums[i]
        let op2 = nums[i]*mul
        ans += Math.max(op1,op2)
        mul--
        
       
    }
    return ans
};
