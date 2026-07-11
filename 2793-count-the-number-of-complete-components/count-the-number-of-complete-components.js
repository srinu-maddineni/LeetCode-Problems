/**
 * @param {number} n
 * @param {number[][]} edges
 * @return {number}
 */
var countCompleteComponents = function(n, edges) {
    let graph = Array.from({length:n},()=>[])

    for(let [u,v] of edges){
        graph[u].push(v)
        graph[v].push(u)
    }
    let visited = new Array(n)
    console.log(graph)
    let sol = 0
    for(let i=0;i<n;i++){
        if(!visited[i]){
            let track = {n:0,e:0}
            dfs(i,track)
            let ued = track.e /2
            let ed =(track.n*(track.n-1))/2
            if(ed === ued){
                sol++
            }
        }
    }

    function dfs(node,track){
        visited[node] = true
        track.n++
        track.e+=graph[node].length
        for(let neh of graph[node]){
            
            if(!visited[neh]){
                dfs(neh,track)
            }
        }
     
    }
    return sol
};