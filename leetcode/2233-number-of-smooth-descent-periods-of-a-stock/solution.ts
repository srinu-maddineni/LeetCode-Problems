function getDescentPeriods(prices: number[]): number {
    let res = 0
    let len =0
    for(let i=1;i<prices.length;i++){
        if(prices[i-1]-prices[i] ===1){
            len++
        }
        else{
            len=0
        }
        res+=len
    }
    return res+prices.length
};
