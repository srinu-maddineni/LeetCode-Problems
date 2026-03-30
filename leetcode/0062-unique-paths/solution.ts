function uniquePaths(m: number, n: number): number {
    let dp :number [][]=[]

    for(let i=0;i<m;i++){
        dp[i]=[]
        for(let j=0;j<n;j++){
           if(i===0||j===0){
            dp[i][j] =1
           }

           else{
            let val = dp[i-1][j]
            val+=dp[i][j-1]
            dp[i][j] = val
           }
        }
    }
    return dp[m-1][n-1]
};
