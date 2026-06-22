/**
 * @param {number[]} nums
 * @return {number}
 */
var thirdMax = function(nums) {
    let f = -Infinity
    let s =-Infinity
    let t =-Infinity
    for(let i=0;i<nums.length;i++){
        if( f===nums[i] || s === nums[i] || nums[i] ===t){
            continue
        }
        if(nums[i]>t){
            f = s
            s = t
            t = nums[i]
        }
        else if(nums[i]>s){
            f = s
            s = nums[i]
        }
        else if(nums[i]>f){
            f =nums[i]
        }
    }
    return f===-Infinity?t:f
};
