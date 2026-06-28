/**
 * @param {number} n
 * @param {number} k
 * @return {number[][]}
 */
var combine = function(n, k) {
   

    let res = []
    function back(s,sol){
        if(sol.length === k){
            res.push([...sol])
            return
        }
        for(let i=s;i<=n;i++){
            
            sol.push(i)
              
            back(i+1,sol)
            sol.pop()
        }
    }
    back(1,[])
    return res
};
