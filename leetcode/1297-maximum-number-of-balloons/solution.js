/**
 * @param {string} text
 * @return {number}
 */
var maxNumberOfBalloons = function(text) {
    let b = {}
    let ba = 'balloon'
    for(let i of text){
        if(ba.includes(i)){
            b[i] = (b[i]||0)+1
        }
       
    }
    b['l'] = Math.floor(b['l']/2)
    b['o'] = Math.floor(b['o']/2)
    let m = Math.min(b['b']||0,b['a']||0,b['l']||0,b['o']||0,b['n']||0)
    
    
    return m
};
