function countCompleteComponents(n: number, edges: number[][]): number {
    let graph = {}
    let visited = new Set()
    let count =0
    for (let i = 0; i < n; i++) {
        graph[i] = [];
    }
    for(let [u,v] of edges){
        graph[u].push(v)
        graph[v].push(u)
    }



    for(let i =0;i<n;i++){
      if(!visited.has(i)){
       let [node,edge] = dfs(graph,i,visited)
       if (edge == node * (node - 1) / 2){
        count++
       }
    }}
    return count
}
function dfs(graph,node,visited){
   let stk = [node]
   visited.add(node)
   let nodes = 0
   let edge = 0
   while(stk.length>0){
    let curr = stk.pop()
    nodes++
    edge +=graph[curr].length
    for(let neh of graph[curr]){
        if(!visited.has(neh)){
            visited.add(neh)
            stk.push(neh)
        }
    }
   }
    return [nodes,edge/2]
}
