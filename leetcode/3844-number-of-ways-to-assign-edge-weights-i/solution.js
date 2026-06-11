/**
 * @param {number[][]} edges
 * @return {number}
 */
var assignEdgeWeights = function(edges) {
    let n = edges.length + 1;
    let graph = Array.from({ length: n + 1 }, () => []);
    for(let [u,v] of edges){
        graph[u].push(v)
        graph[v].push(u)
    }
    let visited = new Set([1])
    let queue = [[1,0]]
    let max = 0
    let f = 0
    while(f<queue.length){
        let [i,d] = queue[f++]
        max = Math.max(d,max)
        for(let n of graph[i]){
            if(!visited.has(n)){
                queue.push([n,d+1])
                visited.add(n)
            }
        }
    }
  let mod = 1000000007
    if (max === 0) return 0;

    return modPow(2, max - 1, mod);
};

function modPow(base, exp, mod) {
    let ans = 1n;
    let b = BigInt(base);
    let m = BigInt(mod);

    while (exp > 0) {
        if (exp & 1) {
            ans = (ans * b) % m;
        }

        b = (b * b) % m;
        exp >>= 1;
    }

    return Number(ans);
}
