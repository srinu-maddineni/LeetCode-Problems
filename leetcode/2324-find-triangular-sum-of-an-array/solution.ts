function triangularSum(nums: number[]): number {
    while(nums.length>1){
        let n = []
        for(let i=1;i<nums.length;i++){
            let m = nums[i]+nums[i-1]
            if(m>=10){
                m = m%10
            }
            n.push(m)
        }
        nums = n
    }
    // console.log(12%10)
    return nums[0]
};
