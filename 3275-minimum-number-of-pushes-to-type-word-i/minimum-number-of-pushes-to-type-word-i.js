/**
 * @param {string} word
 * @return {number}
 */
var minimumPushes = function(word) {
    let res = 0
    let n= word.length
    for(let i=1;i<n+1;i++){

        let m = Math.ceil(i/8)

        res+=m
    }
    return res
};