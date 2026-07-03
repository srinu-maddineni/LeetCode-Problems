/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    let n = nums.length

    for(let i=0;i<n;i++){
       let max =1
       for(let j=i+1;j<n;j++){
        if(nums[i]===nums[j]){
            max++
       }
       else{break}
       }
       if(max>2){
        nums.splice(i+1,max-2)
       }
      
        
    } 

    return nums.length
};
