function countSubmatrices(grid: number[][], k: number): number {
    if(grid[0][0]>k){
        return 0
    }
    let count =1
    console.log(grid.length)
    for(let i=1;i<grid.length;i++){
        grid[i][0] = grid[i][0]+grid[i-1][0]
        if(grid[i][0] <= k){
            count++
        }

    }
    for(let j=1;j<grid[0].length;j++){
        grid[0][j] = grid[0][j]+grid[0][j-1]
        if(grid[0][j]<=k){
            count++
        }

    }
    for(let i =1;i<grid.length;i++){
        let m =0
        for(let j=1;j<grid[0].length;j++){
            grid[i][j]=grid[i-1][j]+grid[i][j-1]+grid[i][j]-grid[i-1][j-1];
            if(grid[i][j]<=k){
                count++
            }
        }

    }
    return count
};
