function lengthOfLIS(nums: number[]): number {
    let n=nums.length
    let dp :number [] = new Array(n).fill(1)
    for(let i =0;i<n;i++){
        
        let max = 1
        for(let j=0;j<i;j++){
            if(nums[j]<nums[i]){
                max = Math.max(max,dp[j]+1)
                
            }
            
        }
        dp[i] = max
    }
    return Math.max(...dp)
};
