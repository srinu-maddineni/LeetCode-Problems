/**
 * @param {number[]} nums
 * @return {number}
 */
var minOperations = function(nums) {
    // This is a more TL and it takes TLE

    // let m = new Map()
    // for(let i of nums){
    //     m.set(i,(m.get(i)|0)+1)
    // }

    // function helper(map){
    //     for(let i of map.values()){
    //         if(i>1){
    //             return false
    //         }
    //     }
    //     return true
    // }
    // let count =0
    // let n = nums.length
    // let i=0
    // while(i<n){
    //     if(helper(m)){
    //         return count
    //         break
    //     }
    //     let j = i
    //     count++
    //     while(j<n && j<i+3){
    //     m.set(nums[j],m.get(nums[j])<=0?0:m.get(nums[j])-1)
    //     j++
    //     }
    //     i=j
    // }
    // return count


    //This one is O(N)

    let seen = new Set()

    for(let i=nums.length-1;i>=0;i--){
        if(seen.has(nums[i])){
            return Math.floor(i/3)+1
        }
        seen.add(nums[i])
    }
    return 0

};