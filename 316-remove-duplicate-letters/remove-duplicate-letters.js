/**
 * @param {string} s
 * @return {string}
 */
var removeDuplicateLetters = function(s) {
const lastOccur = {};

for (let i = 0; i < s.length; i++) {
    lastOccur[s[i]] = i; 
}
let stk = []
let seen = new Set()
for(let i=0;i<s.length;i++){
    let char = s[i]
    if(seen.has(char)) continue
    while(stk.length >0 &&(char < stk[stk.length-1]) && lastOccur[stk[stk.length - 1]] > i){
        let r = stk.pop()
        seen.delete(r)
    }
    stk.push(char);
    seen.add(char);
}
return stk.join('')
};