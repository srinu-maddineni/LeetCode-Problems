/**
 * @param {number[]} gain
 * @return {number}
 */
var largestAltitude = function(gain) {
  let alMax = 0
  let curr = 0
  for(let i of gain){
    curr+=i
    alMax = Math.max(alMax,curr)
  }  
  return alMax
};
