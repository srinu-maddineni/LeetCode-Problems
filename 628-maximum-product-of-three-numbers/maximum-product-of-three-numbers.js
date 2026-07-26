/**
 * @param {number[]} nums
 * @return {number}
 */
var maximumProduct = function(nums) {
    let n = nums.length
    if(n<3){
        return nums[0]*nums[1]
    }
    nums.sort((a,b)=>a-b)
    
    let mx = nums[n-1]*nums[n-2]*nums[n-3]
    let m = nums[0]*nums[1]*nums[n-1]
    return mx>m?mx:m
};