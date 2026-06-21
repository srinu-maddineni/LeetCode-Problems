/**
 * @param {number[]} arr
 * @return {number[]}
 */
var replaceElements = function(arr) {
    let max = 0
    for(let i=arr.length-1;i>=0;i--){
        let m =max
       max = Math.max(arr[i],max)
       arr[i] = m
       
    }
    arr[arr.length-1] = -1
    return arr
};
