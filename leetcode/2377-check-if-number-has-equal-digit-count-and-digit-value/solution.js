/**
 * @param {string} num
 * @return {boolean}
 */
var digitCount = function(num) {
    let m = new Map()

    for(let i=0;i<num.length;i++){
        let currentDigit = Number(num[i])
        m.set(currentDigit, (m.get(currentDigit) || 0) + 1);
    }
    for(let i =0;i<num.length;i++){
        console.log(m.get(i))
        if(Number(num[i]) != (m.get(i)||0)){
            return false
        }
    }
    console.log(m)
    return true
};
