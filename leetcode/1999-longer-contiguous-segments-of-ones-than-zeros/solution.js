/**
 * @param {string} s
 * @return {boolean}
 */
var checkZeroOnes = function(s) {
    let max_0 = 0
    let max_1 = 0

    for(let i=0;i<s.length;i++){
        let max = 0
        for(let j=i;j<s.length;j++){
            if(s[i] === s[j]){
                max++
            }
            else{break}
        }
        if(s[i] ==='1'){
            max_1 = Math.max(max,max_1)
        }
        else{
            max_0 = Math.max(max,max_0)
        }
    }
    return max_1>max_0?true:false
};
