/**
 * @param {string} s
 * @return {string}
 */
var decodeString = function(s) {
    let stk = []

    for(let i=0;i<s.length;i++){
        if(s[i] !== ']'){
            stk.push(s[i])
            continue
        }
        let str = ''


            while(stk[stk.length-1] !== '['){
                str=stk.pop()+str
            }
            stk.pop()

        let num =''

        while (
            stk.length &&
            !isNaN(stk[stk.length - 1]) &&
            stk[stk.length - 1] !== ' '
        ) {
            num = stk.pop() + num;
        }

        let decoded = str.repeat(Number(num));

        // Push decoded string back to stack
        for (let c of decoded) {
            stk.push(c);
        }
    }
    return stk.join('')
};
