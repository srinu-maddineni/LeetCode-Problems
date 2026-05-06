function findWinners(matches: number[][]): number[][] {
    let res = [[],[]]
    let m = new Map()
    let max =0
    for(let i of matches){
        if(!m.has(i[0])){
            m.set(i[0],0)
        }
        m.set(i[1],(m.get(i[1])||0)+1)

    }
    for(let [i,j] of m){
        if(j === 1){
            res[1].push(i)
        }
        if(j === 0){
            res[0].push(i)
        }
    }
    res[0].sort((a,b)=>a-b)
    res[1].sort((a,b)=>a-b)

    return res

};
