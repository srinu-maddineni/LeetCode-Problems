/**
 * @param {number[][]} occupiedIntervals
 * @param {number} freeStart
 * @param {number} freeEnd
 * @return {number[][]}
 */
var filterOccupiedIntervals = function(occupiedIntervals, freeStart, freeEnd) {
    occupiedIntervals.sort((a,b)=>a[0]-b[0])
    let ans = []
    ans.push(occupiedIntervals[0])

    for(let i=1;i<occupiedIntervals.length;i++){
        let op = ans[ans.length-1]
        if(op[1]+1>=occupiedIntervals[i][0]){
            
            op[1] = Math.max(op[1],occupiedIntervals[i][1])
        }
        else{
            ans.push(occupiedIntervals[i])
            
        }
    }
    let fin = []
    for(let [start,end] of ans){
        if (end < freeStart || start > freeEnd) {
            fin.push([start, end]);
        }
        else{
            if(start<freeStart){
                fin.push([start,freeStart-1])
            }
            if(end>freeEnd){
                fin.push([freeEnd+1,end])
            }
        }
    }
        
    console.log(ans)
    return fin
};
