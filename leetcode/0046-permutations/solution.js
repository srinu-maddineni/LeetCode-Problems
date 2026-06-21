/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var permute = function(nums) {
    let res = []


    function back(p){
        if(p.length === nums.length){
            res.push([...p])
        }
        for(let num of nums){
            if(p.includes(num)){continue}
            p.push(num)
            back(p)
            p.pop()
        }

    }
    back([])
    return res
};
