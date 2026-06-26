/**
 * @param {number[]} nums
 * @return {number[]}
 */
var rearrangeArray = function(nums) {
   nums.sort((a,b)=>a-b)
   let c =[]
   let l = 0
   let r =nums.length-1
   while(l<=r){
    if(nums[l]===nums[r]){
        c.push(nums[l])
        break
    }
    c.push(nums[l])
    c.push(nums[r])
    l++
    r--
   }
 
   return c
};
