function rob(nums: number[]): number {
    if(nums.length===1){
        return nums[0]
    }
    if (nums.length === 2) {
    return Math.max(nums[0], nums[1]);
}
    let n = nums.length
    let dp:number [] =[nums[0],Math.max(nums[0],nums[1])]

    for(let i =2;i<n-1;i++){
        dp[i] =Math.max(dp[i-1],dp[i-2]+nums[i])
    }

    let dp1:number [] = []
    dp1[1]=nums[1]
    dp1[2] =Math.max(nums[1],nums[2])

    for(let j=3;j<n;j++){
        dp1[j]=Math.max(dp1[j-1],dp1[j-2]+nums[j])
    }

    return Math.max(dp[n-2],dp1[n-1])

};
