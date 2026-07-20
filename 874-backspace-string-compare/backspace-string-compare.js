/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var backspaceCompare = function(s, t) {
    let stk = []
    let stk1 = []
    for(let i=0;i<s.length;i++){
        if(s[i] === '#'){
            stk.pop()
        }
        else{
            stk.push(s[i])
        }
    }
    for(let i=0;i<t.length;i++){
        if(t[i] === '#'){
            stk1.pop()
        }
        else{
            stk1.push(t[i])
        }
    }
    console.log(stk , stk1)
    return stk.join('') === stk1.join('')
};