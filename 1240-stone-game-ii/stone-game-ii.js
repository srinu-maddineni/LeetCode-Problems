/**
 * @param {number[]} piles
 * @return {number}
 */
var stoneGameII = function(piles) {


    let memo = new Map()
  function helper(a,index,m){
    if(index>=piles.length) return 0
    let key = `${a}-${index}-${m}`
    if(memo.has(key)) return memo.get(key)
    let res = a?0:Infinity
    let sum =0
    for (let i = 1; i <= Math.min(2 * m, piles.length - index); i++){
        sum+=piles[index + i - 1]
        if(a){
            res = Math.max(res,sum+helper(!a,i+index,Math.max(m,i)))
        }
        else{
        res =Math.min(res, helper(!a, index + i, Math.max(m, i)))
        }
    }
    memo.set(key,res)
    return res
  }  
  return helper(true,0,1)
};