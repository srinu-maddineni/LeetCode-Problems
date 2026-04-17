function minMirrorPairDistance(nums: number[]): number {
    let min = Infinity
    let s = {}
    // for(let i=0;i<nums.length;i++){
    //     s[nums[i]]=i
    // }
    for(let i=0;i<nums.length;i++){

        if(nums[i] in s){
            let r = i-s[nums[i]]
            min  = Math.min(min,r)
        }
        let res = Number(String(nums[i]).split('').reverse().join(''))

        s[res] = i 
    }
    return min === Infinity?-1:min
};
