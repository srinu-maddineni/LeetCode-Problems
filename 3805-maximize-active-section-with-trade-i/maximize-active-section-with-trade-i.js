/**
 * @param {string} s
 * @return {number}
 */
var maxActiveSectionsAfterTrade = function(s) {
    
    s = '1'+s+'1'
    let numOne = 0
    for(let i=1;i<s.length-1;i++){
        if(s[i] === '1'){
            numOne++
        }
    }
    let i=0
    let run = []
    while(i<s.length){
        let j=i
        while(j<s.length && s[j] === s[i]){ j++}
        run.push([s[i],j-i])
        i=j
    }
    let ans = numOne;


    for (let k = 1; k < run.length - 1; k++) {
if (
    run[k][0] === '1' &&
    run[k - 1][0] === '0' &&
    run[k + 1][0] === '0'
) {
            let gain = run[k - 1][1] + run[k + 1][1];
            ans = Math.max(ans, numOne + gain);
        }
    }

    return ans;
   

};