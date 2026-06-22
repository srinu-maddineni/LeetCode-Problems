/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var subarraySum = function(nums, k) {
    let total = 0
    let per = 0
    let m = new Map()
    m.set(0,1)
    for(let i=0;i<nums.length;i++){

        per += nums[i]
        let curr = per-k
        if(m.has(curr)){
            total+=m.get(curr)
            
        }
        m.set(per,(m.get(per)||0)+1)
    }
    return total
};
