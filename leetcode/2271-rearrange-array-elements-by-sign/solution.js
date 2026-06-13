/**
 * @param {number[]} nums
 * @return {number[]}
 */
var rearrangeArray = function(nums) {
    let i = []
    let j = []
    for(let num of nums){
        num>=0?i.push(num):j.push(num)
    }
    let a =0

    let c = []
    while(a<i.length ){
        c.push(i[a])
        c.push(j[a])
        a++
    }
    return c
};
