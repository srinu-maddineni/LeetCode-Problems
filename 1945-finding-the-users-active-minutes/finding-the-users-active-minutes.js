/**
 * @param {number[][]} logs
 * @param {number} k
 * @return {number[]}
 */
var findingUsersActiveMinutes = function(logs, k) {
    let m = {}
    const unique = [...new Set(logs.map(JSON.stringify))].map(JSON.parse);
    for(let [u,v] of unique){
        m[u] = (m[u]||0)+1
    }
    let arr = new Array(k).fill(0)
    for(let v of Object.values(m)){
        arr[v - 1]++;
    }
    return arr
};