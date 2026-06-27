/**
 * @param {number[]} nums
 * @return {number}
 */
var maximumLength = function (nums) {
    let m = new Map()
    for (let i = 0; i < nums.length; i++) {
        m.set(nums[i], (m.get(nums[i]) || 0) + 1)
    }
    let one = m.get(1) || 0
    let ans = one % 2 ? one : one-1
    console.log(ans)
    m.delete(1)
    console.log(m)
    for (let num of m.keys()) {
        let r = num
        let res = 0
        while(m.has(r)&&m.get(r)>1){
            res+=2
            r*=r
        }
        ans = Math.max(ans,res+(m.has(r)?1:-1))
    }
    return ans
};