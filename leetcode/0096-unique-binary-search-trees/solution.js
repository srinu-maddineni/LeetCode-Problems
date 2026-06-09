/**
 * @param {number} n
 * @return {number}
 */
var numTrees = function(n) {
    let db = new Array(n+1).fill(0)
    db[0]=1
    db[1]=1
    for(let i=2;i<n+1;i++){
        for(let j=1;j<=i
        ;j++){
            db[i]+= (db[j-1]*db[i-j])
        }
    }
    return db[n]
};

