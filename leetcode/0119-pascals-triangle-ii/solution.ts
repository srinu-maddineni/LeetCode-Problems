function getRow(rowIndex: number): number[] {

    let ps:number [][] =[[1],[1,1]]

// 1
// 1 1
// 1 2 1
// 1 3 3 1
    for(let i=1;i<rowIndex+1;i++){
        ps[i] =[1]
        for(let j=1;j<i;j++){
            ps[i][j] =ps[i-1][j-1]+ps[i-1][j]
        }
        ps[i].push(1)
    }
    return ps[rowIndex]
};
