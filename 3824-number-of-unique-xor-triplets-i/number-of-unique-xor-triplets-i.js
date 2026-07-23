/**
 * @param {number[]} nums
 * @return {number}
 */
var uniqueXorTriplets = function(nums) {
//     let s = new Set()

//     for(let i=0;i<nums.length;i++){
//         for(let j=i;j<nums.length;j++){
//             for(let k =j;k<nums.length;k++)
// {
//                 let x = nums[i]^nums[j]^nums[k]
//                 s.add(x)
// }        }
//     }
//     return s.size
    
    let n = nums.length
    if(n===2){
        return 2
    }
    if(n===1){return 1}
    let msb =-1
    while(n>0){
        n=Math.floor(n / 2)
        msb++
    }
    return 2**(msb+1)
};