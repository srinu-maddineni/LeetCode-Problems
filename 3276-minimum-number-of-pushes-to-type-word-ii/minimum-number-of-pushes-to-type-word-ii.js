/**
 * @param {string} word
 * @return {number}
 */
var minimumPushes = function(word) {
  let map = {}
  for(let i=0;i<word.length;i++){
    if(!map[word[i]]){
        map[word[i]] = 0
    }
    map[word[i]]+=1
  }  

  let freq = Object.values(map).sort((a,b)=>b-a)
  let total =0
  for(let i=1;i<freq.length+1;i++){
    total+=freq[i-1]*(Math.ceil(i/8))
  }
  return total
};