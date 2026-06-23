/**
 * @param {number[]} nums
 * @return {number}
 */
var findMaxLength = function(nums) {
    let c = 0
    let t = 0
    let m = new Map()
    m.set(0,-1)
    for(let i =0 ;i<nums.length;i++){
        c += nums[i] ===0?-1:1

        if(m.has(c)){
            t = Math.max(t,i-m.get(c))
        }
        else{
            m.set(c,i)
        }
    }
    return t
};
