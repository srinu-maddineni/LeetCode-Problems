function isGood(nums: number[]): boolean {
    let m = new Map()
    let max = 0
    for(let i=0;i<nums.length;i++){
        max = Math.max(max,nums[i])
        m.set(nums[i],(m.get(nums[i])||0)+1)
    }
    console.log(max,m)
    if(max+1 != nums.length){
        return false
    }
    for(let [key,val] of m){
        if(key === max){
            if(val != 2){
                return false
            }
        }
        else if(val != 1){
            return false
        }
    }
    return true
};
