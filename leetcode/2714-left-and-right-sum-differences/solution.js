/**
 * @param {number[]} nums
 * @return {number[]}
 */
var leftRightDifference = function(nums) {

    let ans = []
    let r = nums.reduce((acc,curr)=>acc+curr,0)
    console.log(r)
    let l = 0
    for(let i=0;i<nums.length;i++){
        r-=nums[i]
        let n = Math.abs(r-l)
        ans.push(n)
        
        l+=nums[i]
        
        }

    return ans
};
