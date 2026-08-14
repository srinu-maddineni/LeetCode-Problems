/**
 * @param {string} s
 * @return {number}
 */
var maximumLengthSubstring = function(s) {
   
    let max=0
    
    for(let i=0;i<s.length;i++){
        let m=new Map()
        for(let j=i;j<s.length;j++){
            m.set(s[j],(m.get(s[j])|0)+1)
            
            if(m.get(s[j])>2){
                break
            }
            max = Math.max(max,j-i+1)
        }
        console.log(m)
    }
    return max
};