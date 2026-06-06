/**
 * @param {number} n
 * @return {boolean}
 */
var consecutiveSetBits = function(n) {
    let b = String(n.toString(2))
    console.log(b)
    let k = 0
    let i=0
    while(i<b.length){
        if(b[i] === '1'){
            let j = i+1
            while(j<b.length && b[j] !== '0' ){
                if(b[j]==='1'){
                    j++
                }
            }
            console.log(j)
            if(j-i === 2 ){
                k++
            }
            else if(j-i >  2){
                return false
            }
            i = j+1
        }
        else{
            i++
        }
        
    }
    return k===1?true:false
};
