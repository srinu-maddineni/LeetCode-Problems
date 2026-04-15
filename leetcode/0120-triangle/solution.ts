function minimumTotal(triangle: number[][]): number {
    let dp:number [][] = [[triangle[0][0]]]

    for(let i=1;i<triangle.length;i++){
        dp[i] = []
        for(let j=0;j<i+1;j++){
            
            let left = j<dp[i-1].length?(dp[i-1][j]+triangle[i][j]):Infinity
            let right = j-1<0?Infinity: (dp[i-1][j-1]+triangle[i][j])
            dp[i][j] = Math.min(left,right)

        }
        
    }
//   
    return Math.min(...dp[triangle.length-1])
};
