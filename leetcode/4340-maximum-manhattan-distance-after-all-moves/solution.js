/**
 * @param {string} moves
 * @return {number}
 */
var maxDistance = function(moves) {
    let x = 0
    let y = 0
    let wild = 0
    for(let i of moves){
        if(i === 'R') x++
        else if(i === 'L') x--
        else if(i === 'U') y++
        else if(i === 'D') y--
        else if(i === '_') wild++
    }
    return Math.abs(x)+Math.abs(y)+wild
};
