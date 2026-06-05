/**
 * @param {number[]} arr
 * @param {number[][]} mat
 * @return {number}
 */
var firstCompleteIndex = function(arr, mat) {
    let r = new Map()
    let c = new Map()
    let pos = new Map();

    for (let i = 0; i < mat.length; i++) {
        r.set(i, 0);
        for (let j = 0; j < mat[0].length; j++) {
            pos.set(mat[i][j], [i, j]);
        }
    }

    for(let i=0;i<mat.length;i++){
        r.set(i,0)
    }
    for(let i=0;i<mat[0].length;i++){
        c.set(i,0)
    }

    for(let i=0;i<arr.length;i++){
        let [a,b] =  pos.get(arr[i]);
        r.set(a,r.get(a)+1)
        c.set(b,c.get(b)+1)
        if(r.get(a) === mat[0].length || c.get(b) === mat.length){
            return i
        }
    }
    return -1

};

// function q(arr,t){

// for (let i = 0; i < arr.length; i++) {
//     for (let j = 0; j < arr[i].length; j++) {
//         if (arr[i][j] === t) {
//             return [i,j];
//         }
//     }
// }


// }
