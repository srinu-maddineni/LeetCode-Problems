/**
 * @param {string} s
 * @return {number}
 */
var countPalindromicSubsequence = function(s) {
    let n = new Set(s)
    let ans =0
    console.log(n)
    for(let i of n){
        let l = s.indexOf(i)
        let r = s.lastIndexOf(i)
        if(r-l>1){
            let m = s.slice(l+1,r)
            ans+=new Set(m).size
        } 
    }
    return ans
};
