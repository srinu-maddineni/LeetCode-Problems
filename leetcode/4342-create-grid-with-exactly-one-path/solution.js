/**
 * @param {number} m
 * @param {number} n
 * @return {string[]}
 */
var createGrid = function(m, n) {
    const grid = Array.from(
    { length: m },
    () => Array(n).fill('#')
);

    for(let i=0;i<n;i++){
        grid[0][i] ='.'
    }
    for(let j=0;j<m;j++){
        grid[j][n-1] = '.'
    }
        return grid.map(m=>m.join(''))
};
