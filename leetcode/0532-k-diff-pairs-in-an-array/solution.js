/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var findPairs = function(nums, k) {
    let s = new Set()
    let res = 0
    for(let i=0;i<nums.length;i++){
        for(let j=i+1;j<nums.length;j++){
            if(Math.abs(nums[i]-nums[j]) === k ){
                let key = `${Math.min(nums[i],nums[j])},${Math.max(nums[j],nums[i])}`
                if(!s.has(key)){
                res++
                s.add(key)
                }
            }
        }
    }
    return res
};
