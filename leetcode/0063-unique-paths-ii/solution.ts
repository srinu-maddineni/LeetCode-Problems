function uniquePathsWithObstacles(obstacleGrid: number[][]): number {
    let dp:number [][] = []
    for(let i=0;i<obstacleGrid.length;i++){
        dp[i] =[]
        for(let j=0;j<obstacleGrid[0].length;j++){
            
            if(obstacleGrid[i][j] === 1){
                dp[i][j] =0
            }
            else if(i===0 && j ===0){
                dp[i][j]=1
            }

            else{
                dp[i][j] =(i>0?dp[i-1][j]:0)+(j>0?dp[i][j-1]:0)
            }
        }
    }
    return dp[obstacleGrid.length-1][obstacleGrid[0].length-1]
};
