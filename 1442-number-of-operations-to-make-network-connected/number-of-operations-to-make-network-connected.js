/**
 * @param {number} n
 * @param {number[][]} connections
 * @return {number}
 */
var makeConnected = function(n, connections) {
    if (connections.length < n - 1) return -1;
    let graph = Array.from({length:n},()=>[])
    for(let [u,v] of connections){
        graph[u].push(v)
        graph[v].push(u)
    }

    function dfs(i){
        v.add(i)
        for(let neh of graph[i]){
            if(!v.has(neh)){
                dfs(neh)
            }
        }

    }
    let v = new Set()
    let res = 0
    for(let i=0;i<n;i++){
        if(!v.has(i)){
            res++
            dfs(i)
        }
    }
    return res-1
};