/**
 * @param {number[]} nums
 * @return {number}
 */
var maxRotateFunction = function(nums) {

    let s = 0
    let f = 0
    for(let i=0;i<nums.length;i++){
        s+=nums[i]
        f+=nums[i]*i

    }
    let max = f
    let n = nums.length
    for(let i=n-1;i>0;i--){
        f = f+s - n*nums[i]
        max = Math.max(max,f)
    }
    return max
};



