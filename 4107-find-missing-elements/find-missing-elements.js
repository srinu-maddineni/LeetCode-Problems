/**
 * @param {number[]} nums
 * @return {number[]}
 */
var findMissingElements = function(nums) {
    nums.sort((a,b)=>a-b)
    let result =[]
    let curr = nums[0]
    for(let i=1;i<nums.length;){
        // if((nums[i-1] !== nums[i]-1) ){
        //     result.push(nums[i-1]+1)
        // }
        // if(result.length>0 && nums[i] !== result[result.length-1]+1){
        //     result.push(result[result.length-1]+1)
        // }
        
        if(curr+1 !== nums[i]){
            result.push(curr+1)
            
        }
        else{
            i++
        }
        curr = curr+1
    }
    return result
};