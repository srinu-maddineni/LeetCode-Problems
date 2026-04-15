function closestTarget(words: string[], target: string, startIndex: number): number {
    let n = words.length
    let min = Infinity
    console.log(words[(0+1)%n])
    for(let i=0;i<n;i++){
        if(words[i] === target){
            let dit = Math.abs(i-startIndex)
            let cir = Math.min(dit,n-dit)
            min=Math.min(min,cir)
        }
    }
    return min===Infinity?-1:min
};
