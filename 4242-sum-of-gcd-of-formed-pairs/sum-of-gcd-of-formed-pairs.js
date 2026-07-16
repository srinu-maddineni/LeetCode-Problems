/**
 * @param {number[]} nums
 * @return {number}
 */
var gcdSum = function(nums) {
    

function gcd(a, b) {
    if (b === 0) {
        return a;
    }

    return gcd(b, a % b);
}
    let n= nums.length
    let mx =0
    let arr=[]
    for(let i=0;i<n;i++){
        mx = mx>nums[i]?mx:nums[i]
        arr.push(gcd(nums[i],mx))
    }
    console.log(arr)
    arr.sort((a,b)=>a-b)
    let sum =0
    let i=0;
    let j=nums.length-1;
    while(i<j){
        sum+= gcd(arr[i],arr[j])
        i++
        j--
    }
    return sum

};