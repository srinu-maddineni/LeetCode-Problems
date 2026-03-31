function numSquares(n: number): number {
    let dp :number [] =[]
    dp[0]=0
    for(let i=1;i<=n;i++){
        let j =1;
        let min =Infinity
        while (j**2<=i){
          min = Math.min(min,dp[i-(j**2)])
          j++
        }
        dp[i] = 1+min
    }
    return dp[n]
};
