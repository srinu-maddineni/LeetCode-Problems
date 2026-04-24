function furthestDistanceFromOrigin(moves: string): number {
    let  l = 0
    let r = 0
    let d =0
    for(let i of moves){
        if(i === "L"){
            l++
        }
        else if(i === "R"){
            r++
        }
        else{
            d++
        }
    }
    if(l>=r){
        return (l+d)-r
    }
    else{
        return (r+d)-l
    }
};
