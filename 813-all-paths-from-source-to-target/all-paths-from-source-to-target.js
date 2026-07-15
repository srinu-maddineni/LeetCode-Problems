/**
 * @param {number[][]} graph
 * @return {number[][]}
 */
var allPathsSourceTarget = function(graph) {
    let t = graph.length-1
    let arr = []
    function dfs(i,a){
        
        if(i === t){
            arr.push([...a])
            return
        }
        for(let neh of graph[i]){
            a.push(neh)
            dfs(neh,a)
            a.pop()
        }
    }

   
        dfs(0,[0])

    return arr

};