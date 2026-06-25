/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var countMajoritySubarrays = function(nums, target) {
  let ans = 0
  for(let i=0;i<nums.length;i++){
    let t = 0
    for(let j=i;j<nums.length;j++){
        if(nums[j] === target){
            t++
        }
        if((j-i+1) < t*2){
            ans++
        }
    }
  }  
  return ans
};