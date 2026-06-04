/**
 * @param {string} word
 * @return {number}
 */
var longestBeautifulSubstring = function(word) {

    let ans = 0
    let m = 1
    let v =1

        for(let j=1;j<word.length;j++){
            if(word[j-1]>word[j]){
                m = 1
                v = 1
            }
            else{
                m++
                if(word[j]>word[j-1]){
                    v++
                }
            }
        
        if(v === 5){
            ans = Math.max(ans,m)
        }
        }
    return ans
};
