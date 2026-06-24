/**
 * @param {string} s
 * @return {string}
 */
var largestEven = function(s) {
    let i = -1
    for(i=s.length-1;i>=0;i--){
        if(s[i]%2===0){
            break
        }
    }
    return i=== -1?"":s.slice(0,i+1)
};
