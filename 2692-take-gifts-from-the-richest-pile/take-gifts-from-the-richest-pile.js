/**
 * @param {number[]} gifts
 * @param {number} k
 * @return {number}
 */
var pickGifts = function(gifts, k) {
    let res =0 
    gifts.sort((a,b)=>a-b)
    let mx = gifts[gifts.length-1] 
    for(let i=1;i<=k;i++){
        let k = Math.floor(Math.sqrt(mx))
        gifts[gifts.length-1] = k
        gifts.sort((a,b)=>a-b)
        mx = gifts[gifts.length-1]
    }
    for(let i=0;i<gifts.length;i++){
        res+=gifts[i]
    }
    return res
};