/**
 * @param {number} n
 * @param {number} k
 * @return {number}
 */
var sumOfGoodIntegers = function(n, k) {
    let totalSum = 0
    let st = Math.max(1,n-k)
    let en = n+k
    
    for(let i=st;i<=en;i++){
        console.log(i)
        if((i & n) == 0){
            totalSum+=i
        }

    }
    return totalSum
};
