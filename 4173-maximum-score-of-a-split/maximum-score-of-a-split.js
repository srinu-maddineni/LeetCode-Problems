/**
 * @param {number[]} nums
 * @return {number}
 */
var maximumScore = function(nums) {
    let maxScore = -Infinity
    let n = nums.length
    let suff = new Array(n)
    suff[n-1] = nums[n-1]
    let j =0
    for(let i=n-2;i>=0;i--){
        suff[i] = Math.min(nums[i], suff[i + 1]);    }
    console.log(suff)
    let pre = 0
    for(let i=0;i<n-1;i++){
      pre += nums[i]
      let sc = pre - suff[i+1]
      maxScore = Math.max(sc,maxScore)
    }
    return maxScore
};