function isValid(s: string): boolean {
    let stk:string [] = []
    let m = {
        '}':'{'
        ,']':'[',
        ')':'('
    }
    for(let i=0;i<s.length;i++){
        let char = s[i]
        if(char in m){
            if(stk.length ===0){
                return false
            }
            let top = stk[stk.length-1]
            if(top!=m[char]){
                return false

            }
            else{
                stk.pop()
            }
        }
        else{
            stk.push(char)
        }
    }
    return stk.length ===0
};
