/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    let ar = [] ;
    for(let i= 0 ; i < arr.length ; i++){
        ar.push(fn(arr[i],i));
        
    }
    return ar;
};

function fn(num,i){
    return i+num;
}
