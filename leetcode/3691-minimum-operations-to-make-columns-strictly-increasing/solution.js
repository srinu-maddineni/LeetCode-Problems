/**
 * @param {number[][]} grid
 * @return {number}
 */
var minimumOperations = function(grid) {
    let count = 0
    for(let i=0;i<grid[0].length;i++){
        for(let j=1;j<grid.length;j++){
            if(grid[j][i]<=grid[j-1][i]){
            let t = grid[j-1][i]+1
            let diff = t - grid[j][i]
            count+=diff
            grid[j][i] = t
            }
        }
    }
    return count
};
