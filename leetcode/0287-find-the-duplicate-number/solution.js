/**
 * @param {number[]} nums
 * @return {number}
 */
var findDuplicate = function(nums) {
    nums.sort((a,b)=>a-b)
    console.log(nums)
    for(let i=1;i<nums.length;i++){
        if((nums[i]^nums[i-1]) === 0){
            return nums[i]
        }
    }
};
