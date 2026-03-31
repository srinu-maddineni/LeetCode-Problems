function isUgly(n: number): boolean {
    if(n<=0){
        return false
    }
    for(let i of [2,3,5]){
        while(n%i===0){
                n=n/i
        }
    }
    return n ===1
};
