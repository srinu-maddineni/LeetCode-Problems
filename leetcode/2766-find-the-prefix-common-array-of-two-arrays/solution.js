/**
 * @param {number[]} A
 * @param {number[]} B
 * @return {number[]}
 */
var findThePrefixCommonArray = function(A, B) {
    let s = new Set()
    let n = 0
    let res = []
        for(let i=0;i<A.length;i++){
            if(A[i] === B[i]){
                n++
            }
            if(s.has(A[i])){
                n++
            }
            if(s.has(B[i])){
                n++
            }
            s.add(A[i])
            s.add(B[i])
            res.push(n)
        }
        return res
    
};
