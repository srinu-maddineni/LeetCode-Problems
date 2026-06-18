/**
 * @param {number[][]} intervals
 * @return {number[][]}
 */
var merge = function(intervals) {
    intervals.sort((a,b)=>a[0]-b[0])
    console.log(intervals)
    let result = []
    result.push(intervals[0])
    let i=1
    while(i<intervals.length){
        let n = intervals[i]
        
        let m = result[result.length-1]
        if( n[0]<=m[1]){
            m[1] = Math.max(n[1],m[1])
            i++
        }
        else{
            result.push(n)
            i++

        }
    }
    return result
    
};
