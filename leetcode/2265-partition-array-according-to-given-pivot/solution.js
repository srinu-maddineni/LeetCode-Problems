/**
 * @param {number[]} nums
 * @param {number} pivot
 * @return {number[]}
 */
var pivotArray = function(nums, pivot) {
    let pos =0
    for(let i=0;i<nums.length;i++){
        if(nums[i]<pivot){
            let temp = nums[i]
            for(let j=i;j>pos;j--){
                nums[j]=nums[j-1]
            }
            nums[pos]=temp
            pos++
        }
    }
    for(let i=0;i<nums.length;i++){
        if(nums[i] === pivot){
            let temp = nums[i]
            for(let j=i;j>pos;j--){
                nums[j] = nums[j-1]
            }
            nums[pos] = temp
            pos++
        }
    }
    return nums
};
