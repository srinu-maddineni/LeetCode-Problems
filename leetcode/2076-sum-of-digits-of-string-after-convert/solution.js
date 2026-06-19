/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var getLucky = function(s, k) {
    let num = ''
    for(let i of s){
        num+=i.charCodeAt(0)-96

    }
    
    while(k>0){
        let m = 0
        for(let i=0;i<num.length;i++){
            m+=Number(num[i])
        }
        num=String(m)
        k--
    }
    return Number(num)
};
