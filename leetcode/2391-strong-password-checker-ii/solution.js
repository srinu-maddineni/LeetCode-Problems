/**
 * @param {string} password
 * @return {boolean}
 */
var strongPasswordCheckerII = function(password) {
    if(password.length < 8){
        return false
    }
    const sp = "!@#$%^&*()-+"
    // const c = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    let n = false
    let m = false
    let k = false
    let r = false

    for(let i=0;i<password.length;i++){
        if(i>0&&password[i] === password[i-1]){
            return false
        }
        if(password[i].charCodeAt(0)>=65 && password[i].charCodeAt(0)<=90){
            n = true
        }
        if(password[i].charCodeAt(0)>=97 && password[i].charCodeAt(0)<=122){
            m = true
        }
        if(sp.includes(password[i])){
            k = true
        }
        if (/[0-9]/.test(password[i])) {
            r = true;
        }

    }
    if(n && m && k && r){
        return true
    }
    return false
};
