/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let prof = 0
    let currMin = prices[0]
    for(let i=0;i<prices.length;i++){
        let curr = prices[i] - currMin
        prof  = Math.max(prof,curr)
        currMin = Math.min(currMin,prices[i])
    }
    return prof
};
