/**
 * @param {number[]} edges
 * @return {number}
 */
var edgeScore = function(edges) {
    let n = edges.length
    let arr = new Array(n).fill(0)
    for(let i=0;i<n;i++){
        arr[edges[i]] = arr[edges[i]]+i
    }
    let mx = Math.max(...arr)
    // arr.sort((a,b)=>)
    // console.log(arr,mx)
    for(let i =0;i<n;i++){
        if(arr[i]===mx){
            return i 
        }
    }
};