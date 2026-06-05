/**
 * @param {number[][]} matrix
 * @return {boolean}
 */
var checkValid = function(matrix) {
    let n = matrix.length
    let m = matrix[0].length
   
    for(let i=0;i<n;i++){
        let row = new Set()
        let col = new Set()
        for(let j=0;j<m;j++){
            row.add(matrix[i][j])
            col.add(matrix[j][i])
        }
        if(row.size !== n || col.size !== m){
            return false
        }
        
    }
    return true
};
