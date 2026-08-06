/**
 * @param {number} n
 * @param {number} t
 * @return {number}
 */
var smallestNumber = function(n, t) {
    function helper(m){
        let product = 1
            while (m > 0) {
            product *= m % 10;
            m = Math.floor(m / 10);
        }
        return product
    }
    while(true){

        if(helper(n)%t ===0){
            return n
        }
        else{
            n++
        }
    }
};