/**
 * @param {number} n
 * @return {number}
 */
var maxProduct = function(n) {
    let s = String(n).split('').sort((a,b)=>Number(a)-Number(b))
    return Number(s[s.length-1]) * Number(s[s.length-2])

    
};