/**
 * @param {number} n
 * @param {number} k
 * @return {string[]}
 */
var generateValidStrings = function(n, k) {
let res = []
    function backtrack(currString,currCost,lastChar){
        if(currString.length === n){
            res.push(currString)
            return 
        }
        backtrack(currString+'0',currCost,'0')
        const nextIndex = currString.length
        if(lastChar != '1' && (currCost+nextIndex <=k)){
            backtrack(currString+'1',currCost+nextIndex,'1')
        }
    }
    backtrack('',0,'')
    return res
};
