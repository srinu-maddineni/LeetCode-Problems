/**
 * @param {number} n
 * @param {number[][]} trust
 * @return {number}
 */
var findJudge = function(n, trust) {
  let m = new Map()
//   for(let i=1;i<=n;i++){
//     m.set(i,0)
//   }
//   for(let [u,v] of trust){
//     m.set(u,m.get(u)+1)
//   }
//   console.log(m)
//   for(let k =1;k<=n;k++){
//     if(m.get(k) ===0){
//         return k
//     }
//   }
if(n===1){
    return 1
}
 let arr  = new Array(n+1).fill(0)

 for(let [u,v] of trust){
    arr[u]--
    arr[v]++
 }
 for(let i=0;i<=n;i++){
    if(arr[i] === n-1){
        return i
    }
 }
  return -1
};