/**
 * @param {number[]} nums
 * @return {number[]}
 */
var rearrangeArray = function(nums) {
    let res = []
    let pos = 0
    let nev = 1
    for(let i=0;i<nums.length;i++){
        if(nums[i]<0){
            res[nev] = nums[i]
            nev+=2
        }
        else{
            res[pos] = nums[i]
            pos+=2
        }
    }
    return res
};
