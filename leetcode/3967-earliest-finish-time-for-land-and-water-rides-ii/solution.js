/**
 * @param {number[]} landStartTime
 * @param {number[]} landDuration
 * @param {number[]} waterStartTime
 * @param {number[]} waterDuration
 * @return {number}
 */
var earliestFinishTime = function(landStartTime, landDuration, waterStartTime, waterDuration) {
    let n =landStartTime.length
    let m = waterStartTime.length
    let ans1 = Infinity
    let ans2 = Infinity
    let finish1 = Infinity
    let finish2 = 0
    let finish3 = Infinity
    let finish4 = 0


    for(let i=0;i<n;i++){
       let time1 = landStartTime[i]+landDuration[i]
        finish1 = Math.min(time1,finish1)
    }


    for(let j=0;j<m;j++){
            
            finish2 = Math.max(finish1,waterStartTime[j])+waterDuration[j]
            ans1 = Math.min(ans1,finish2)

        }
    
  

    for(let i=0;i<m;i++){
        let time = waterStartTime[i]+waterDuration[i]
        finish3 = Math.min(time,finish3)
    }
    for(let j=0;j<n;j++){
        let finish4 = Math.max(finish3,landStartTime[j])+landDuration[j] 
        ans2 = Math.min(ans2,finish4)
    }

    return Math.min(ans1,ans2)
};
