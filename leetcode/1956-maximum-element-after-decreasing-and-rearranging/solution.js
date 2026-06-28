/**
 * @param {number[]} arr
 * @return {number}
 */
var maximumElementAfterDecrementingAndRearranging = function(arr) {
    arr.sort((a,b)=>a-b)
    for(let i=0;i<arr.length;i++){
        if(i===0){
            arr[i]=1
            continue
        }
        if(arr[i-1]===arr[i] || arr[i-1]===arr[i]+1){
            continue
        }
        else{
            arr[i] = arr[i-1]+1
        }
    }
    console.log(arr)
    return arr[arr.length-1]
};
