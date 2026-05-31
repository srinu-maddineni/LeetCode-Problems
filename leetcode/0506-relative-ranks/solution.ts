function findRelativeRanks(score: number[]): string[] {
    let sc = [...score]
    let s = []
    score.sort((a,b)=>b-a)
    console.log(score)
    for(let i of sc){
        if(score[0] === i){
            s.push("Gold Medal")
        }
        else if(score[1] === i){
            s.push("Silver Medal")
        }
        else if(score[2] === i){
            s.push("Bronze Medal")
        }
        else{
            s.push(String(score.indexOf(i)+1))
        }
    }
    return s
    
};
