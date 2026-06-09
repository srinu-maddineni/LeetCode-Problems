/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var maxTotalValue = function(nums, k) {
    let max = 0
    let min = Infinity
    for(let i of nums){
        max=Math.max(max,i)
        min = Math.min(min,i)
    }
    return (max-min)*k
};
