/**
 * @param {string} s
 * @return {number}
 */
var numberOfSubstrings = function(s) {
    let count = 0
    let m = {'a':-1,'b':-1,'c':-1}
    for(let i=0;i<s.length;i++){
            m[s[i]] =i
            if(m['a']!=-1&&m['b']!=-1&&m['c']!=-1){
                let min = Math.min(m['a'],m['b'],m['c'])
                count+=min+1
            }
    }
return count
};