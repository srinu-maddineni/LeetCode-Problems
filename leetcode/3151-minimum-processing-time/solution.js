/**
 * @param {number[]} processorTime
 * @param {number[]} tasks
 * @return {number}
 */
var minProcessingTime = function(processorTime, tasks) {
    tasks.sort((a,b)=>b-a)
    processorTime.sort((a,b)=>a-b)
    let max = 0
    let j =0
    for(let i=0;i<processorTime.length;i++){
        let s =processorTime[i]+ Math.max(tasks[j],tasks[j+1] ,tasks[j+2],tasks[j+3])
        j+=4
        max= Math.max(max,s)
        
    }
    return max
};
