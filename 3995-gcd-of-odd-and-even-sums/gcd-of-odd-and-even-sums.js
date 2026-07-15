/**
 * @param {number} n
 * @return {number}
 */
var gcdOfOddEvenSums = function(n) {
    function gcd(a,b){
        let mod = a%b

        if(mod === 0){

            return b
        }
        else{
            return gcd(b,mod)
        }
    }
    console.log(gcd(n*n , n*(n+1)))
    return gcd(n*n , n*(n+1))
    
    // return res
};