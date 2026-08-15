/**
 * @param {number[]} nums
 * @return {number}
 */
var longestSubsequence = function(nums) {
    let ans = 0
    let z = 0
    for(let i=0;i<nums.length;i++){
        if(nums[i]>0) z++
        ans = ans ^ nums[i]
    }
    // console.log(ans, nums.length,z)
    if(z===0) return 0
    return ans ===0?nums.length-1:nums.length
};