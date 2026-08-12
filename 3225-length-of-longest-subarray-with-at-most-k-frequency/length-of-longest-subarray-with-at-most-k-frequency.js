/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var maxSubarrayLength = function(nums, k) {
    let mx =0
    let i =0
    let m = new Map()
    let j=0
    while(i<nums.length){


            m.set(nums[i],(m.get(nums[i])||0)+1)

            while(m.get(nums[i]) > k){
                m.set(nums[j], m.get(nums[j]) - 1);
                j++
            }
            i++
        
        mx = Math.max(mx,i-j)
        // if(j ===nums.length) break
        

        // while(i<j){
        //     if(nums[i] === nums[j]){
        //         m.set(nums[i],m.get(nums[i])-1)
        //         i++
        //         break

        //     }
            
        //     i++
            
        // }
    }
    return mx
};