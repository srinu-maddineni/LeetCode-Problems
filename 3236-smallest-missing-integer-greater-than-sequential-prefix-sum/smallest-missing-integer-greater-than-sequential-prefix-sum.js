/**
 * @param {number[]} nums
 * @return {number}
 */
var missingInteger = function(nums) {
    let sum = nums[0]
    // let max = 0
    // let i=0
    // while(i<nums.length){
    //     let j=i+
    //     let m = 0
    //     let s = 0
    //     while(j<nums.length){
    //     if(nums[j] === nums[j-1]+1){
    //         m++
    //         s+=nums[i]
    //     }
    //     else{
    //         break
    //     }
    //     }
    //     if(m>max){
    //         sum = s
    //     }
    // }
    let j =0
    for(let i=1;i<nums.length;i++){
        if(nums[i] === nums[i-1]+1){
            sum+=nums[i]
            j++
        }
        else{
            break
        }
    }
    nums.sort((a,b)=>a-b)
    for(let i of nums){
        if(i === sum){
            sum++
        }
    }
    return sum
};