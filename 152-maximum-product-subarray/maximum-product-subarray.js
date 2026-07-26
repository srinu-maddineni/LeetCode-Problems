/**
 * @param {number[]} nums
 * @return {number}
 */
var maxProduct = function(nums) {
    let n = nums.length
    let res = nums[0]
    let mx = nums[0]
    let mn = nums[0]
    for(let i=1;i<n;i++){
        if(nums[i]<0){
            let temp = mx
            mx=mn
            mn=temp
        }
        mx = Math.max(nums[i]*mx,nums[i])
        mn = Math.min(nums[i]*mn,nums[i])
        res = Math.max(res,mx)
    }
    return res
};