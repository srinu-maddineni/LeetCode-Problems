/**
 * @param {number[]} deck
 * @return {boolean}
 */
var hasGroupsSizeX = function(deck) {
    let m = {}
    for(let i=0;i<deck.length;i++){
        m[deck[i]] = (m[deck[i]] || 0) + 1
    }
    let g =0
    function gcd(a,b){
        if(b==0){
            return a
        }
        return gcd(b,a%b)
    }

    for(let i of Object.values(m)){
       g = gcd(g,i)
    }
    return g>=2?true:false

};