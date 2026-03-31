function coinChange(coins: number[], amount: number): number {
    let dp :number [] = []
    dp[0] = 0;
    for(let i =1;i<=amount;i++){
        let min = Infinity
        for(let j of coins){
            if(j<=i){
           min =Math.min(dp[i-j],min)
        }}
        dp[i] = 1+min
    }
    if(dp[amount] == Infinity){
        return -1
    }
    else{
    return dp[amount]
    }
};
