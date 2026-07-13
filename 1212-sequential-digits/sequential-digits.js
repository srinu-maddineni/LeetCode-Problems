/**
 * @param {number} low
 * @param {number} high
 * @return {number[]}
 */
var sequentialDigits = function(low, high) {
    let arr = []
    let s = '123456789'
    for(let i=0;i<s.length;i++){
        let n = s[i]
        for(let j=i+1;j<s.length;j++){
             n = n+s[j]
            let m = Number(n)
            if(m>=low && m<=high){
                arr.push(m)
            }
        }
    }
    return arr.sort((a,b)=>a-b)
};