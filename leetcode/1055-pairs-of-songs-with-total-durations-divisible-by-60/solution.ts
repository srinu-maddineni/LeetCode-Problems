function numPairsDivisibleBy60(time: number[]): number {
    let map = new Array(60).fill(0);

    let c =0
    for(let i=0;i<time.length;i++){
        let rem = time[i]%60
        let need = (60-rem)%60
        c+=map[need]
        map[rem]++
    }
    return c
};
