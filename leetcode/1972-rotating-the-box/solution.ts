function rotateTheBox(boxGrid: string[][]): string[][] {
    let n = boxGrid.length
    let m = boxGrid[0].length
    for(let i=0;i<n;i++){
        let j = m-1
        let low = m-1
        while(j>=0){
            if(boxGrid[i][j] === "."){
                if(j>low){
                    low =j
                }
                j--
            }
            if(boxGrid[i][j] === "*"){
                j--
                low=j
            }
            if(boxGrid[i][j] === "#"){
                boxGrid[i][j] = "."
                boxGrid[i][low] = "#"
                low--
                j--
            }
        }
    }
    let res = Array.from({ length: m }, () => Array(n).fill('.'));  
    for(let i=0;i<n;i++){
        for(let j=0;j<m;j++){
            res[j][n-i-1] = boxGrid[i][j]
        }
    }
    console.log(boxGrid)
    return res
};
