/**
 * @param {character[][]} board
 * @return {void} Do not return anything, modify board in-place instead.
 */
var solve = function(board) {
    let n = board.length
    let m = board[0].length
    let set = new Set()
    function dfs(i,j){
        if(i<0 || j<0 || i >= n || j >= m || board[i][j] === "X" ||
    set.has(`${i},${j}`)){
            return
        }
       
        else{
           
           set.add(`${i},${j}`)
            
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
        }
  
    }
    


    for(let i=0;i<n;i++){
            if(board[i][0]==="O"){
                dfs(i,0)
            }
            if(board[i][m-1] === "O"){
                dfs(i,m-1)
            }    
    }
    for(let i=0;i<m;i++){
        if(board[0][i] === "O"){
            dfs(0,i)
        }
        if(board[n-1][i] === "O"){
            dfs(n-1,i)
        }
    }
    for(let i=0;i<n;i++){
        for(let j=0;j<m;j++){
            if(board[i][j] === "O" && !set.has(`${i},${j}`)){
                board[i][j] = "X"
            }
        }
    }
    console.log(set)
    console.log(board)
    
};