/**
 * @param {number[]} nums
 * @return {number}
 */
var findGCD = function(nums) {
    let mx =0
    let mn =Infinity
    for(let i of nums){
        mx = mx<i?i:mx
        mn = mn>i?i:mn
    }
    console.log(mx,mn)
    function gcd(a,b){
        if(b===0){
            return a
        }
        return gcd(b,a%b)
    }
    return gcd(mx,mn)
};