/**
 * @param {number} n
 * @return {boolean}
 */
var checkGoodInteger = function(n) {
    let sq = 0
    let di = 0
    while(n>0){
        let r = n%10
        n =Math.floor(n / 10)
        sq+= r*r
        di+=r
    }
    return sq-di>=50
    
};
