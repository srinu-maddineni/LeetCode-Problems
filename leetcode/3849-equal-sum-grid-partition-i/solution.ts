function canPartitionGrid(grid: number[][]): boolean {
    let totalSum = 0
    let h = 0
    let v = 0
    let hL = grid.length
    let vL = grid[0].length
    for(let i =0;i<hL;i++){
        for(let j =0;j<vL;j++){
            totalSum +=grid[i][j]
        }
    }
    let target = totalSum/2
    for(let i =0;i<hL-1;i++){
        for(let j =0;j<vL;j++){
            h+=grid[i][j]
        }
        if(target === h){
            return true
        }}
    for(let i =0;i<vL-1;i++){
        for(let j = 0;j<hL;j++){
            v+=grid[j][i]
        
        }
        if(v === target){
            return true
        }
    }

    return false
};
