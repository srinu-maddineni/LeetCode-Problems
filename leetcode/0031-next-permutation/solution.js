/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var nextPermutation = function(nums) {
    let index = -1
    for(let i =nums.length-1;i>0;i--){
        if(nums[i]>nums[i-1]){
            index =i-1
            break
        }
    }
    if(index === -1){
        return nums.sort((a,b)=>a-b)
    }

    for(let i=nums.length-1;i>=index;i--){
        if(nums[i] > nums[index]){
            [nums[i],nums[index]] = [nums[index],nums[i]]
            break
        }
    }
   let start = index + 1;
    let end = nums.length - 1;
    while (start < end) {
        [nums[start], nums[end]] = [nums[end], nums[start]];
        start++;
        end--;
    }
    return nums
};
