/**
 * @param {number} c
 * @return {boolean}
 */
var judgeSquareSum = function(c) {
    for(let i=0;i*i<=c;i++){
        let t = c - (i*i)
        let ta = Math.floor(Math.sqrt(t))

        if(ta*ta === t){
            return true
        }
    }
    return false
};