function canFinish(numCourses: number, prerequisites: number[][]): boolean {
    let graph = {}
    for(let i=0;i<numCourses;i++){
        graph[i] = []
    }
    for(let [u,v] of prerequisites){
        graph[u].push(v)
    }
    let visited = new Set()
    let review = new Set()
    function dfs(node){
        if(review.has(node)){return true}
        if(visited.has(node)){return false}
        visited.add(node)
        review.add(node)
        for(let n of graph[node]){
            if(dfs(n)){
                return true
            }
        }
        review.delete(node)
        return false

    }
    for(let node of Object.keys(graph)){
        if(dfs(node)){
            return false
        }
    }
    console.log(graph)
    return true
};
