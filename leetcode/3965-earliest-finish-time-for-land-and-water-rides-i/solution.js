/**
 * @param {number[]} landStartTime
 * @param {number[]} landDuration
 * @param {number[]} waterStartTime
 * @param {number[]} waterDuration
 * @return {number}
 */
var earliestFinishTime = function(landStartTime, landDuration, waterStartTime, waterDuration) {
    let n = landStartTime.length
    let m = waterStartTime.length
    let minTime = Infinity
    for(let i=0;i<n;i++){
        let time = landStartTime[i]+landDuration[i]
        for(let j=0;j<m;j++){
              let finishTime1 =Math.max(time, waterStartTime[j]) +waterDuration[j];
              let time1 = waterStartTime[j]+waterDuration[j]
                let finishTime = Math.max(landStartTime[i],time1)+landDuration[i]
            minTime = Math.min(minTime, finishTime1,finishTime);
        }
    }
    return minTime
};
