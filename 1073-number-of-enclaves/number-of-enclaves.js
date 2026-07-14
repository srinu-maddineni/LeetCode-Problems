/**
 * @param {number[][]} grid
 * @return {number}
 */
var numEnclaves = function(grid) {
    let sol = 0

    function dfs(i,j){
        if(i<0 || j<0 || i >= grid.length || j >= grid[0].length || grid[i][j] ==0){
            return
        }
       
        else{
           
           
            grid[i][j] = 0
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
        }
  
    }
    let n = grid.length
    let m = grid[0].length


    for(let i=0;i<n;i++){
            if(grid[i][0]===1){
                dfs(i,0)
            }
            if(grid[i][m-1] === 1){
                dfs(i,m-1)
            }    
    }
    for(let i=0;i<m;i++){
        if(grid[0][i] === 1){
            dfs(0,i)
        }
        if(grid[n-1][i] === 1){
            dfs(n-1,i)
        }
    }
    console.log(grid)
    for(let i=0;i<n;i++){
        for(let j=0;j<m;j++){
            if(grid[i][j] === 1){
                sol++
            }
        }
    }
    return sol
};