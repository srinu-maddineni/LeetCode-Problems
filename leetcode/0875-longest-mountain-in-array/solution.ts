function longestMountain(arr: number[]): number {
    let n = 0
    for(let i =0;i<arr.length;i++){
        let j = i+1
        let k = i
        let up = 1
        let down  = 1
        while(arr[k]< arr[j] && j<arr.length){
            up++
            j++;
            k++;
        }
        while(arr[k]>arr[j]&& j<arr.length){
            down++;
            j++;
            k++
        }
        if(up>1 && down >1){
            n= Math.max(n,up+down-1)
        }
        
    }
    if(n===1){
        return 0
    }
    return n
};
