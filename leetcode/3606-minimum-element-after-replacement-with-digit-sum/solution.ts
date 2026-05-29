function minElement(nums: number[]): number {
    let min = Infinity
    for(let i of nums){
        console.log(i)
        let k = 0
        for(let j of String(i)){
            k+=Number(j)
        }
        min = Math.min(k,min)
    }
    return min
};
