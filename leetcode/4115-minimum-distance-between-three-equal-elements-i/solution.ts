function minimumDistance(nums: number[]): number {
    if(nums.length<3){
        return -1
    }
    let min =Infinity
    for(let i=0;i<nums.length;i++){
        let arr = [i]
    
        for(let j=i+1;j<nums.length;j++){
            if(arr.length === 3){
                break
            }
            if(nums[i] === nums[j]){
                arr.push(j)
            }
        }
        if(arr.length ===3){
            let s = Math.abs(arr[0]-arr[1])+Math.abs(arr[1]-arr[2])+Math.abs(arr[2]-arr[0])
            
            min = Math.min(s,min)
        }
    }
return min === Infinity ? -1:min
};
