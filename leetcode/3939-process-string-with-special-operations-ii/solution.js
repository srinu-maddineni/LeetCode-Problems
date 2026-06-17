/**
 * @param {string} s
 * @param {number} k
 * @return {character}
 */
var processStr = function(s, k) {
    let result = []
    let len = 0
    for(let str of s){
        if(str === '#'){
            len*=2
        }
        else if(str === '%'){
            len = len
        }
        else if(str === '*'){
            if(len>0){
            len--
        }}
        else{
            len++
        }
        result.push(len)
    }
    if(k>=len||k<0){
        return "."
    }
    for(let i=s.length-1;i>=0;i--){
        let char = s[i]
        let prev = i > 0 ? result[i - 1] : 0;
        if(char ==='#'){
            k%=prev
        }
        else if(char === '%'){
            k = prev -1-k
        }
        else if(char === '*'){
            // k++
        }
        else{
        if(k === prev){
            return char
        }
        }
    }
    return "."
};
