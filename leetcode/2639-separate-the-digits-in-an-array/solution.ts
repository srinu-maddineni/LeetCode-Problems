function separateDigits(nums: number[]): number[] {
    let n = []

    for(let i of nums){
        let s = String(i)
        for(let j of s){
            n.push(Number(j))
        }
    }

    return n
};
