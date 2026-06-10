/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var missingMultiple = function(nums, k) {
    let s = new Set(nums)
    let c = 1
    while(s.has(c*k)){
        
            c++

    }
    return c*k
};
