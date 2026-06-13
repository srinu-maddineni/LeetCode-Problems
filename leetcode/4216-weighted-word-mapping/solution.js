/**
 * @param {string[]} words
 * @param {number[]} weights
 * @return {string}
 */
var mapWordWeights = function(words, weights) {
    let s = ''
    let s1 = 'zyxwvutsrqponmlkjihgfedcba'
    for(let i of words){
        let sum = 0
        for(let j of i){
            sum+=weights[j.charCodeAt(j)-97]
        }
        s+=s1[sum%26]
    }
    return s
};
