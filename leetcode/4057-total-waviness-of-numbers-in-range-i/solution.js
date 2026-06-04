/**
 * @param {number} num1
 * @param {number} num2
 * @return {number}
 */
var totalWaviness = function(num1, num2) {

    let c =0
    for(let i = num1;i<num2+1;i++){
            let s = String(i)
            if (s.length < 3) continue;
            for (let j = 1; j < s.length - 1; j++) {
            let prev = s.charCodeAt(j - 1) - 48;
            let curr = s.charCodeAt(j) - 48;
            let next = s.charCodeAt(j + 1) - 48;

 
            if (prev < curr && curr > next) c++;

            else if (prev > curr && curr < next) c++;
        }
    }
    return c
};
