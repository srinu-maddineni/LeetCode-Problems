/**
 * @param {number[][]} grid
 * @param {number} k
 * @return {number[][]}
 */
var shiftGrid = function(grid, k) {
    let arr = []
    for(let g of grid){
        arr.push(...g)
    }
    
    for(let i=0;i<k;i++){
        let temp = arr.pop()
        arr.unshift(temp)
    }

    let m = grid[0].length
    let x=0
    for(let i=0;i<grid.length;i++){
        for(let j=0;j<m;j++){
            grid[i][j] = arr[x]
            x++
        } 
    }
    return grid
};