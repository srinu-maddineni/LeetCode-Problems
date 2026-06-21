/**
 * @param {number[]} nums
 * @param {number} x
 * @return {number}
 */
var countValidSubarrays = function(nums, x) {

    let res = 0

    for(let i=0;i<nums.length;i++){
        let sum=0
            for(let j=i;j<nums.length;j++){
                sum+=nums[j]
                if(sum %10 === x){
                    let f = sum;
                    while(f>=10){
                        f = Math.floor(f/10)
                    }
                    if(f ===x){
                        res++
                    }
                }
            }
    }
    return res
};
