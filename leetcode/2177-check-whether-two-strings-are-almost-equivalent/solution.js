/**
 * @param {string} word1
 * @param {string} word2
 * @return {boolean}
 */
var checkAlmostEquivalent = function(word1, word2) {
   let n = new Array(26).fill(0)

    for(let i=0;i<word1.length;i++){
        let index1 = word1.charCodeAt(i) - 97;
        let index2 = word2.charCodeAt(i) - 97;
        n[index1]++
        n[index2]--
    }
    for(let i of n){
        if(i>3 || i<-3){
            return false
        }
    }
    return true


};
