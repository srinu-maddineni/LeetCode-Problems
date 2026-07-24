/**
 * @param {number[][]} edges
 * @param {number} bob
 * @param {number[]} amount
 * @return {number}
 */
var mostProfitablePath = function(edges, bob, amount) {
    

    let n = amount.length
    let bobArr = new Array(n).fill(-1)
    let graph = Array.from({length:n},()=>[])
    for(let [u,v] of edges){
        graph[u].push(v)
        graph[v].push(u)
    }

    function bobpat(node,par,t){
        bobArr[node] =t

        if(node === 0){ return true}
        
        for(let neh of graph[node]){
            if(neh !== par){
                if(bobpat(neh,node,t+1)){
                    return true
                }
            }
            
        }

        bobArr[node] = -1
        return false
    }
    bobpat(bob,-1,0)
    console.log(bobArr)
    let stk = [0]
    let alinaAns = 0
    let time =0
    console.log(graph)
    function alinaDfs(node ,par,time,curr){
        let bobTime = bobArr[node]
        if(time === bobTime){
            curr+=Math.floor(amount[node]/2)
        }
        else if(bobArr[node] === -1 || time< bobTime){
            curr += amount[node]
        }
        let isleaf = true
        let mx = -Infinity
        for(let neh of graph[node]){

            if(neh !== par){
                isleaf = false
                mx = Math.max(mx,alinaDfs(neh,node,time+1,curr))
            }
        }

        return isleaf?curr:mx
        

    }
    return alinaDfs(0,-1,0,0)
    
};