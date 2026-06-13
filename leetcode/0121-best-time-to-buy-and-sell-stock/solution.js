/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let profit = 0
    let minPrice = Infinity
    for(let price of prices){
         minPrice = Math.min(price,minPrice)
        let p =price- minPrice
        profit = Math.max(p,profit)
    }
    return profit
};
