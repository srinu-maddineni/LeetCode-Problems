function minimumEffort(tasks: number[][]): number {
    tasks.sort((a,b)=>(b[1]-b[0])-(a[1]-a[0]))
    let n = tasks[0][1]
    let f = n-tasks[0][0] 

    for(let i=1;i<tasks.length;i++){
            if(f >= tasks[i][1]){
                f-=tasks[i][0]
            }
            else{
            let k = tasks[i][1] - f
            n+=k
            f = tasks[i][1]- tasks[i][0]
            }

    }
    return n

};
