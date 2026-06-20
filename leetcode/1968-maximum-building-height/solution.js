/**
 * @param {number} n
 * @param {number[][]} restrictions
 * @return {number}
 */
var maxBuilding = function(n, restrictions) {
    if(restrictions.length<=0) return n-1
    restrictions.push([1,0])
    restrictions.sort((a,b)=>a[0]-b[0])
    let prevH = 0
    for(let i=1;i<restrictions.length;i++){
       let d = restrictions[i][0]-restrictions[i-1][0]
       restrictions[i][1] = Math.min(restrictions[i][1],restrictions[i-1][1]+d)

    }
    for(let i=restrictions.length-2;i>=0;i--){
       let d = restrictions[i+1][0]-restrictions[i][0]
       restrictions[i][1] = Math.min(restrictions[i][1],restrictions[i+1][1]+d)

    }
    let maxAns = 0
    for(let i=1;i<restrictions.length;i++){
        let d = restrictions[i][0] - restrictions[i-1][0];
let peak = Math.floor((restrictions[i-1][1] + restrictions[i][1] + d) / 2);
maxAns = Math.max(maxAns, peak);
    }
  let lastRestriction = restrictions[restrictions.length - 1];
    

    let lastPeak = lastRestriction[1] + (n - lastRestriction[0]);
    

    return Math.max(maxAns, lastPeak);
};
