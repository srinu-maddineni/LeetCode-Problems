/**
 * @param {number[][]} brackets
 * @param {number} income
 * @return {number}
 */
var calculateTax = function(brackets, income) {
    if(income === 0){
        return 0.00000
    }
    let tax = 0
    let prev =0
    for(let [up,per] of brackets){
        if(income <= prev){
            break
        }
        let amount = Math.min(up,income) - prev
        tax += (amount *(per/100))
        prev = up
        
    }
    return tax
};
