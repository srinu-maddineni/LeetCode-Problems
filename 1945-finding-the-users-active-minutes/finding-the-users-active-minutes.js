/**
 * @param {number[][]} logs
 * @param {number} k
 * @return {number[]}
 */
var findingUsersActiveMinutes = function(logs, k) {
    let m = new Map()
    
    for(let [u,v] of logs){
     if(!m.has(u)) m.set(u,new Set())
     m.get(u).add(v)
    }
    let arr = new Array(k).fill(0)
    for(let v of m.values()){
        arr[v.size - 1]++;
    }
    return arr
};