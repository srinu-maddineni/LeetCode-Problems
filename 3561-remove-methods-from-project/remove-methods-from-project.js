/**
 * @param {number} n
 * @param {number} k
 * @param {number[][]} invocations
 * @return {number[]}
 */
var remainingMethods = function(n, k, invocations) {
    let arr = Array.from({length:n},()=>true)
    console.log(arr)

    let graph = Array.from({length:n},()=>[])
    for(let [u,v] of invocations){
        graph[u].push(v) 
    }
    console.log(graph)
    let vis = new Set()

    function dfs(node){
            if (vis.has(node)) return;
            vis.add(node);

            arr[node] = false;
        for( let i of graph[node]){
            dfs(i)
        }
    }
    dfs(k)
    for (let [u, v] of invocations) {
        if (arr[u] && !arr[v]) {
            return Array.from({ length: n }, (_, i) => i);
        }
    }
    let res = []
    for(let i=0;i<n;i++){
        if(arr[i]){
            res.push(i)
        }
    }
    return res
};