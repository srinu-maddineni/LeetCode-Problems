/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
var setZeroes = function(matrix) {
    let m = []
    for(let i=0;i<matrix.length;i++){
        for(let j=0;j<matrix[0].length;j++){
            if(matrix[i][j] ===0){
            m.push([i,j])
            }
        }
    }
    let n = matrix.length
    let x = matrix[0].length
    for(let p of m){
        let j = p[1]
        let i = p[0]
        let a = i
        while(a>=0){
            matrix[a][j]=0
            a--
        }
        let b =i
        while(b<n){
            matrix[b][j]=0
            b++
        }
        let c =j
        while(c>=0){
            matrix[i][c]=0
            c--
        }
        let d =j
        while(d<x){
            matrix[i][d] =0
            d++
        }
    }
    return matrix
};
