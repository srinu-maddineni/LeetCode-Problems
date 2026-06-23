/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var numSubarrayProductLessThanK = function(nums, k) {
    if(k===0){return 0}
    let t=0
    for(let i=0;i<nums.length;i++){
        let prod = 1
        for(let j=i;j<nums.length;j++){
            prod *= nums[j]
            if(prod<k){
                t++
            }
            else{break}
        }
    }
    return t
};
