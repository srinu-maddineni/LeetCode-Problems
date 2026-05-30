function searchMatrix(matrix: number[][], target: number): boolean {
    let n = matrix.length
    let m = matrix[0].length
    // if(m<=0){

    // }
    console.log(m,n)
    let i =0


    
    while(i<n){
        if(matrix[i][0] === target){
            return true
        }
        if(matrix[i][m-1]>=target){
            // console.log('in')
            for(let k =0 ;k<m;k++){
                if(matrix[i][k] === target){
                    return true
                }
            }
            return false
        }
        if(matrix[i][m-1]<target){
            i++
        }
        else{
            return false
        }
    }
    return false
};
