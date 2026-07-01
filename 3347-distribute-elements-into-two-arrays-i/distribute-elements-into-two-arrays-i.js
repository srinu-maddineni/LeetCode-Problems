/**
 * @param {number[]} nums
 * @return {number[]}
 */
var resultArray = function(nums) {

    let arr1 = []
    arr1.push(nums[0])
    let arr2 =[]
    arr2.push(nums[1])
    let i =0
    let j=0
    let n = 2
    
    while(n<nums.length){
        
        if(arr1[i]>arr2[j]){

            arr1.push(nums[n])
            i++
            n++
        }
        else{
            arr2.push(nums[n])
            j++
            n++
        }
    }

    return [...arr1,...arr2]

};