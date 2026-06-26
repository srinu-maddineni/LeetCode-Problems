/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var permuteUnique = function(nums) {
    let res = []
    nums.sort((a,b)=>a-b)

    let visited = new Array(nums.length).fill(false)
    function back(p){
        if(p.length === nums.length){
            res.push([...p])
            return
        }
        for(let i=0;i<nums.length;i++){
            if(visited[i]) {continue}
            if(i>0 &&nums[i] === nums[i-1]&&!visited[i-1]) continue
            p.push(nums[i])
            visited[i] = true
            back(p)
            p.pop()
            visited[i] =false
        }
    }
    back([])
    return res
};