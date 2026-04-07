function isPossibleToSplit(nums: number[]): boolean {
    if(nums.length%2 != 0){
        return false
    }
    let m = {}
    for(let i of nums){
        m[i] = (m[i]||0)+1
        if(m[i] >2){
            return false
        }
    }
    console.log(m)
    return true
};
