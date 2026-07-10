/**
 * @param {string} s
 * @return {string}
 */
var maskPII = function(s) {
    if(s.includes('@')){
       s = s.toLowerCase()
        let i=0
       let [name,domain] = s.split('@')
        return `${name[0]}*****${name[name.length - 1]}@${domain}`;    }
    const digits = s.replace(/\D/g, ''); 
    const local = "***-***-" + digits.slice(-4);

    const countryCodeLength = digits.length - 10;
    if (countryCodeLength === 0) return local;
    
    return `+${"*".repeat(countryCodeLength)}-${local}`;
};