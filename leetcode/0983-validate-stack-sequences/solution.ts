function validateStackSequences(pushed: number[], popped: number[]): boolean {
    let stk = []
    let j =0
    for(let i =0;i<pushed.length;i++){
        if(pushed[i] === popped[j]){
            j++
            for(let k =stk.length-1;k>=0;k--){
                if(stk[k]===popped[j]){
                    stk.pop()
                    j++
                }
            }
        }
        else{
            stk.push(pushed[i])
        }
    }
    return stk.length===0?true:false
};
