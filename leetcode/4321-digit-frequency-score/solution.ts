function digitFrequencyScore(n: number): number {
    let s = String(n)
    let m = new Map()
    for(let i of s){
        if(m.has(i)){
            m.set(i,m.get(i)!+1)
        }
        else{
            m.set(i,1)
        }
    }
    let r = 0
    for(let [k,v] of m){
        r+=Number(k)*Number(v)
    }
    return r
};
