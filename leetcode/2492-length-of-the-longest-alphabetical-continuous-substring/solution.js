/**
 * @param {string} s
 * @return {number}
 */
var longestContinuousSubstring = function(s) {
    let long = 0
    let curr =1
    for(let i =0;i<s.length;i++){
        if(s.charCodeAt(i) === (s.charCodeAt(i-1)+1 )){
            curr++
        }
        else{
            curr =1
        }
        long = Math.max(long,curr)
    }
    return long
};
