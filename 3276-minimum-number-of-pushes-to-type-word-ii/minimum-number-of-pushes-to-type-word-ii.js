/**
 * @param {string} word
 * @return {number}
 */
var minimumPushes = function(word) {

    let n = word.length
    let count =0
    let arr = Array.from({ length: 26 }, (_, i) => [
    String.fromCharCode(i + 97),
    0
]);
    for (let ch of word) {
    arr[ch.charCodeAt(0) - 97][1]++;
   }
   arr.sort((a,b)=>b[1]-a[1])

    for(let i=1;i<=26;i++){
        let j = Math.ceil(i/8)
        count += j*arr[i-1][1]
    }
    return count
};