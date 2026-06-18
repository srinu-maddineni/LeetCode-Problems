/**
 * @param {number[][]} intervals
 * @param {number[]} newInterval
 * @return {number[][]}
 */
var insert = function(intervals, newInterval) {
    intervals.push(newInterval)
    intervals.sort((a,b)=>a[0]-b[0])
    let result = []
    result.push(intervals[0])
    for(let i=1;i<intervals.length;i++){
        let curr = intervals[i]
        let last = result[result.length-1]
        if(curr[0]<=last[1]){
            last[1] = Math.max(last[1],curr[1])
        }
        else{
            result.push(curr)
        }
    }
    return result
};
