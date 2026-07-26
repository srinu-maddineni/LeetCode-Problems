/**
 * @param {number[]} nums
 * @return {number}
 */
var maxProduct = function(nums) {
    let n = nums.length
    let mx =0
    let mx1 =0
    for(let i=0;i<n;i++){
        let num = Math.abs(nums[i])

        if(num>mx){
            mx1 = mx
            mx=num
        }
        else if(num>mx1){
            mx1=num
        }
    }

    return mx*mx1*100000
    

};