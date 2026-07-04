/**
 * @param {number} n
 * @param {number[][]} roads
 * @return {number}
 */
var minScore = function(n, roads) {
    let graph =  Array.from({ length: n + 1 }, () => [])
    for(let [u,v,w] of roads){

        graph[u].push([v,w])
        graph[v].push([u,w])
    }
    let visited = new Set()
    visited.add(1)
    let queue = []
    queue.push(1)
    let min = Infinity
    while(queue.length>0){
        let node = queue.shift()

        for(let [n,w] of graph[node]){
            min = Math.min(min,w)
            if(!visited.has(n)){
                visited.add(n)
                queue.push(n)
            }
        }
    }
    return min
};
