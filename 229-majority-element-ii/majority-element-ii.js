/**
 * @param {number[]} nums
 * @return {number[]}
 */
var majorityElement = function(nums) {
    let m = new Map()
    let n =Math.floor( nums.length/3)
    for(let num of nums){
        m.set(num,(m.get(num)||0)+1)
    }
    let ans = []
    for(let num of m.keys()){
        let x = m.get(num)
        if(x>n){
            ans.push(num)
        }
    }
    console.log(m)
    return ans
};