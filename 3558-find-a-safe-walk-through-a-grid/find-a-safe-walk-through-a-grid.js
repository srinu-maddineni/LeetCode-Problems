/**
 * @param {number[][]} grid
 * @param {number} health
 * @return {boolean}
 */
var findSafeWalk = function(grid, health) {
    let n = grid.length
    let m = grid[0].length
    let dir = [
        [0,1],
        [1,0],
        [0,-1],
        [-1,0]
    ]

    let queue = []
    queue.push([0,0])
    let dist = Array.from({length:n} ,()=>Array(m).fill(Infinity))
    dist[0][0] = grid[0][0];
    while(queue.length>0){
        let [r,c] = queue.shift()
        for(let [u,v] of dir){
            let [newR,newC] = [r+u,c+v]
            if(newR<0 || newC<0 || newR>=n || newC >=m){ continue}
            let w = grid[newR][newC]
            let cost = w + dist[r][c]

            if(cost <dist[newR][newC] ){
                dist[newR][newC] = cost
                if(w === 0){
                    queue.unshift([newR,newC])
                }
                else{
                    queue.push([newR,newC])
                }
            }
        }
    }
    return health-dist[n-1][m-1]  >0?true:false

};