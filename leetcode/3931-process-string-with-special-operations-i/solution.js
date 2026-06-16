/**
 * @param {string} s
 * @return {string}
 */
var processStr = function(s) {
    let result = []
    for(let str of s){
        if(str === '#'){
            result = [...result,...result]
        }
        else if(str === '*'){
            if(result){
                result.pop()
            }
        }
        else if(str === '%'){
            result.reverse()
        }
        else{
            result.push(str)
        }
    }
    return result.join('')
};
